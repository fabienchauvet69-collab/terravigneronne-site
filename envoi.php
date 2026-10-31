<?php
// Formulaire de contact : envoie la demande à contact@terravigneronne.com
$to = 'contact@terravigneronne.com';
$back = '/contact';

function fail($back) { header('Location: ' . $back . '?envoi=erreur', true, 303); exit; }
function clean($v, $max) { return mb_substr(trim(str_replace(["\r", "\n"], ' ', (string)$v)), 0, $max); }

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { header('Location: ' . $back, true, 303); exit; }
// Piège à robots : un humain ne remplit pas ce champ caché
if (!empty($_POST['site'])) { header('Location: ' . $back . '?envoi=ok', true, 303); exit; }

$nom = clean($_POST['nom'] ?? '', 120);
$email = clean($_POST['email'] ?? '', 160);
$tel = clean($_POST['tel'] ?? '', 30);
$type = clean($_POST['type'] ?? '', 40);
$commune = clean($_POST['commune'] ?? '', 80);
$message = mb_substr(trim((string)($_POST['message'] ?? '')), 0, 4000);

if ($nom === '' || $message === '' || !filter_var($email, FILTER_VALIDATE_EMAIL) || empty($_POST['rgpd'])) { fail($back); }

$subject = '=?UTF-8?B?' . base64_encode('Demande de devis – ' . $nom) . '?=';
$body = "Nouvelle demande depuis terravigneronne.com\n\n"
  . "Nom : $nom\nE-mail : $email\nTéléphone : $tel\nType de logement : $type\nCommune : $commune\n\n"
  . "Message :\n$message\n";
$headers = "From: Site Terra Vigneronne <$to>\r\n"
  . "Reply-To: $email\r\n"
  . "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit\r\n";

// Envoi authentifié par la boîte contact@ (évite les indésirables).
// Identifiants dans un fichier hors du site : domains/terravigneronne.com/smtp-config.php
// qui contient : <?php return ['user' => 'contact@terravigneronne.com', 'pass' => '...'];
function smtp_send($cfg, $to, $subject, $body, $headers) {
  $s = @stream_socket_client('ssl://smtp.hostinger.com:465', $errno, $errstr, 15);
  if (!$s) { return false; }
  stream_set_timeout($s, 15);
  $read = function () use ($s) { $r = ''; while (($l = fgets($s, 515)) !== false) { $r .= $l; if (isset($l[3]) && $l[3] === ' ') break; } return (int)substr($r, 0, 3); };
  $cmd = function ($c, $ok) use ($s, $read) { fwrite($s, $c . "\r\n"); return $read() === $ok; };
  $data = "To: <$to>\r\nSubject: $subject\r\nDate: " . date('r') . "\r\n"
    . 'Message-ID: <' . bin2hex(random_bytes(12)) . "@terravigneronne.com>\r\n" . $headers . "\r\n"
    . preg_replace('/^\./m', '..', str_replace(["\r\n", "\n"], ["\n", "\r\n"], $body));
  $ok = $read() === 220
    && $cmd('EHLO terravigneronne.com', 250)
    && $cmd('AUTH LOGIN', 334)
    && $cmd(base64_encode($cfg['user']), 334)
    && $cmd(base64_encode($cfg['pass']), 235)
    && $cmd('MAIL FROM:<' . $cfg['user'] . '>', 250)
    && $cmd("RCPT TO:<$to>", 250)
    && $cmd('DATA', 354)
    && $cmd($data . "\r\n.", 250);
  fwrite($s, "QUIT\r\n");
  fclose($s);
  return $ok;
}

$cfgFile = dirname(__DIR__) . '/smtp-config.php';
$cfg = is_file($cfgFile) ? include $cfgFile : null;
// Si le SMTP échoue (mot de passe changé…), on se rabat sur mail() pour ne perdre aucune demande
$sent = (is_array($cfg) && smtp_send($cfg, $to, $subject, $body, $headers)) || mail($to, $subject, $body, $headers);

if ($sent) { header('Location: ' . $back . '?envoi=ok', true, 303); exit; }
fail($back);
