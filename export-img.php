<?php
// Outil temporaire (espace de test uniquement) : renvoie une image de l'ancien site en base64.
if (($_GET['t'] ?? '') !== '5c25ee98c29b757e5975fdbc') { http_response_code(403); exit; }
$f = $_GET['f'] ?? '';
if (!preg_match('/^[A-Za-z0-9_.\-]+$/', $f)) { http_response_code(400); exit; }
$w = max(100, min(2000, (int)($_GET['w'] ?? 800)));
$url = "https://assets.zyrosite.com/cdn-cgi/image/format=jpeg,quality=80,w=$w/zTo0Ltb35tv1lQDR/$f";
$data = @file_get_contents($url);
header('Content-Type: text/plain');
if ($data === false) { http_response_code(502); echo "ERR"; exit; }
$b = base64_encode($data);
$o = max(0, (int)($_GET['o'] ?? 0));
echo "LEN=" . strlen($b) . "\n" . substr($b, $o, 60000);
