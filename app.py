from flask import Flask, request, send_file, render_template
import yt_dlp
import os
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['url']
        quality = request.form['quality']
        output_path = "downloads"
        os.makedirs(output_path, exist_ok=True)
        
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s_{quality}p.%(ext)s',
            'format': f'bestvideo[height<={quality}]+bestaudio/best' if quality != "best" else 'best',  # Intenta obtener la mejor calidad disponible
            'cookiefile': 'cookies.txt',  # Ruta al archivo de cookies
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(video_url, download=True)
                video_file = ydl.prepare_filename(info_dict)
            return send_file(video_file, as_attachment=True)
        except Exception as e:
            return f"Error al descargar el video: {e}", 400
    else:

        #Lista de videos destacados
        # Lista de videos destacados con enlaces embebidos completos
        videos_destacados = [
            {"embed_link": "https://www.youtube.com/embed/AHNSAwddOck"},
            {"embed_link": "https://www.youtube.com/embed/MjQkqU8y4tE"},
            {"embed_link": "https://www.youtube.com/embed/CSqpCvdc520"},
            {"embed_link": "https://www.youtube.com/embed/q4zzxED_OHU"},
            {"embed_link": "https://www.youtube.com/embed/YF_Fab3Y9Ec"},
            {"embed_link": "https://www.youtube.com/embed/zCoeh4zLHs0"},
            {"embed_link": "https://www.youtube.com/embed/xR63nMzK1Ic"},
            {"embed_link": "https://www.youtube.com/embed/b5OtnuU4-_g"},
            {"embed_link": "https://www.youtube.com/embed/jCp66wTYfcc"}
        ]

        # Selecciona videos aleatorios
        destacados = random.sample(videos_destacados, 2)

        return render_template('index.html', destacados=destacados)
@app.route('/terminos', methods=['GET'])
def terminos():
    return render_template('terminos.html')



if __name__ == '__main__':
    app.run(debug=True)
