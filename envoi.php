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

if (mail($to, $subject, $body, $headers)) { header('Location: ' . $back . '?envoi=ok', true, 303); exit; }
fail($back);
