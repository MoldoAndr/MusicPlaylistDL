from flask import Flask, request, render_template_string
import os
import yt_dlp
import webbrowser

app = Flask(__name__)

def download_playlist(playlist_url, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'ignoreerrors': True,
        'verbose': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([playlist_url])
        except Exception as e:
            return f"An error occurred while downloading {playlist_url}: {e}"

    return "Download complete."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        playlist_url = request.form['playlistUrl']
        output_dir = request.form['outputDir']
        result = download_playlist(playlist_url, output_dir)
        return f"<pre>{result}</pre>"

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <link rel="preconnect" href="https://fonts.gstatic.com">
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet"> 
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Download YouTube Playlist</title>
            <style>
                body {
                    font-family: 'Montserrat', sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    overflow: hidden;
                }
                .container {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 30%;
                    width:30%;
                    margin:auto;
                    position: relative;
                    z-index: 1;
                }
                form {
                    background-color: transparent;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                    width: 300px;
                    z-index: 2;
                }
                label {
                    font-weight: bold;
                    margin-top: 10px;
                    display: block;
                }
                input[type="text"],
                input[type="submit"] {
                    width: 100%;
                    padding: 8px;
                    margin: 10px 0;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    box-sizing: border-box;
                }
                input[type="submit"] {
                    background-color: blue;
                    color: #fff;
                    cursor: pointer;
                    font-size: 16px;
                }
                input[type="submit"]:hover {
                    background-color: #218838;
                }

                canvas {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100vw;
                    height: 100vh;
                    background-color: black;
                    z-index: 0;
                }
            </style>
        </head>
        <body>
            <canvas id="test"></canvas>
            <div class="container">
                <form method="POST">
                    <label for="playlistUrl">Playlist URL:</label>
                    <input type="text" id="playlistUrl" name="playlistUrl" required>

                    <label for="outputDir">Output Directory:</label>
                    <input type="text" id="outputDir" name="outputDir" required>

                    <input type="submit" value="Download">
                </form>
            </div>
        </body>
        <script>
            var w = window.innerWidth,
                h = window.innerHeight,
                canvas = document.getElementById('test'),
                ctx = canvas.getContext('2d'),
                rate = 60,
                arc = 100,
                time,
                count,
                size = 7,
                speed = 20,
                parts = new Array,
                colors = ['red','#f57900','yellow','#ce5c00','#5c3566'];
            var mouse = { x: 0, y: 0 };

            canvas.setAttribute('width', w);
            canvas.setAttribute('height', h);

            function create() {
                time = 0;
                count = 0;

                for(var i = 0; i < arc; i++) {
                    parts[i] = {
                        x: Math.ceil(Math.random() * w),
                        y: Math.ceil(Math.random() * h),
                        toX: Math.random() * 5 - 1,
                        toY: Math.random() * 2 - 1,
                        c: colors[Math.floor(Math.random() * colors.length)],
                        size: Math.random() * size
                    }
                }
            }

            function particles() {
                ctx.clearRect(0,0,w,h);
                canvas.addEventListener('mousemove', MouseMove, false);
                for(var i = 0; i < arc; i++) {
                    var li = parts[i];
                    var distanceFactor = DistanceBetween(mouse, parts[i]);
                    distanceFactor = Math.max(Math.min(15 - (distanceFactor / 10), 10), 1);
                    ctx.beginPath();
                    ctx.arc(li.x, li.y, li.size * distanceFactor, 0, Math.PI * 2, false);
                    ctx.fillStyle = li.c;
                    ctx.strokeStyle = li.c;
                    if(i % 2 == 0)
                        ctx.stroke();
                    else
                        ctx.fill();

                    li.x = li.x + li.toX * (time * 0.05);
                    li.y = li.y + li.toY * (time * 0.05);

                    if(li.x > w){
                        li.x = 0; 
                    }
                    if(li.y > h) {
                        li.y = 0; 
                    }
                    if(li.x < 0) {
                        li.x = w; 
                    }
                    if(li.y < 0) {
                        li.y = h; 
                    }
                }
                if(time < speed) {
                    time++;
                }
                setTimeout(particles, 1000 / rate);
            }

            function MouseMove(e) {
                mouse.x = e.layerX;
                mouse.y = e.layerY;
            }

            function DistanceBetween(p1, p2) {
                var dx = p2.x - p1.x;
                var dy = p2.y - p1.y;
                return Math.sqrt(dx * dx + dy * dy);
            }

            create();
            particles();    
        </script>
        </html>
    ''')

if __name__ == '__main__':
    brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"  # Modify if needed
    webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
    webbrowser.get('brave').open("http://localhost:5000")

    app.run(debug=False)