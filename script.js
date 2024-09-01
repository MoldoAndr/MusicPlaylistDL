document.getElementById("downloadForm").addEventListener("submit", function(event){
    event.preventDefault();  // Prevent the form from submitting the traditional way
    var playlistUrl = document.getElementById("playlistUrl").value;
    var outputDir = document.getElementById("outputDir").value;

    fetch('download.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `playlistUrl=${encodeURIComponent(playlistUrl)}&outputDir=${encodeURIComponent(outputDir)}`
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById("response").innerHTML = data;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById("response").innerHTML = "An error occurred while processing your request.";
    });
});
