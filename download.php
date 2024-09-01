<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $playlistUrl = escapeshellarg($_POST['playlistUrl']);
    $outputDir = escapeshellarg($_POST['outputDir']);

    $command = "python download.py $playlistUrl $outputDir";
    $output = shell_exec($command);

    echo "<pre>$output</pre>";
}
?>