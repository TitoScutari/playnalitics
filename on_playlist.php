<?php
$playlist_id = $_GET["playlist_id"];
$strCommand = "C:\\Python39\\python.exe on_playlist.py $playlist_id";
//$strCommand = "C:\\Python39\\python.exe test_php.py prova_da_terminale";
var_dump($strCommand);
Shell_exec($strCommand);
//var_dump(shell_exec($strCommand))
?>