<?php
$playlist_id = $_GET["playlist_id"];
$strCommand = "python on_playlist.py $playlist_id";
var_dump($strCommand);
shell_exec($strCommand);
?>