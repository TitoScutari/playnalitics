<?php
$playlist_id = $_GET["playlist_id"];
$strCommand = "python on_playlist.py $playlist_id";
shell_exec($strCommand);
?>