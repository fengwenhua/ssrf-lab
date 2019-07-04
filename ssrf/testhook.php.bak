<?php
function getUrlContent($url){
    $url = escapeshellarg($url);
    $pl = "curl ".$url;
    $content = shell_exec($pl);
    return $content;
}

if (isset($_POST['handler'])&&!empty($_POST['handler']))
{
    $url = $_POST['handler'];
    $content_url = getUrlContent($url);
    echo $content_url;
}
?>
