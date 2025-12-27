import subprocess
import json
import os
import sys

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

video_path = r"C:\dron_website\app\views\static\videos\video_background.mp4"

if os.path.exists(video_path):
    print(f"[OK] Video encontrado: {video_path}")
    print(f"[OK] Tamaño: {os.path.getsize(video_path) / (1024*1024):.2f} MB")
    print("\n" + "="*60)

    # Intentar obtener información del video con ffprobe si está disponible
    try:
        result = subprocess.run(
            ['ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_format', '-show_streams', video_path],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            data = json.loads(result.stdout)

            # Buscar stream de video
            video_stream = next((s for s in data.get('streams', []) if s.get('codec_type') == 'video'), None)

            if video_stream:
                print("INFORMACIÓN DEL VIDEO:")
                print("="*60)
                print(f"Resolución: {video_stream.get('width')}x{video_stream.get('height')}")
                print(f"Codec: {video_stream.get('codec_name')}")
                print(f"FPS: {eval(video_stream.get('r_frame_rate', '0/1')):.2f}")
                print(f"Bitrate: {int(video_stream.get('bit_rate', 0)) / 1000000:.2f} Mbps")
                print(f"Duración: {float(video_stream.get('duration', 0)):.2f} segundos")

                # Recomendaciones
                print("\n" + "="*60)
                print("RECOMENDACIONES PARA MÁXIMA CALIDAD:")
                print("="*60)

                width = video_stream.get('width', 0)
                bitrate = int(video_stream.get('bit_rate', 0)) / 1000000

                if width < 1920:
                    print(f"[!] Resolucion actual: {width}p")
                    print("  -> Se recomienda minimo 1920x1080 (Full HD)")
                    print("  -> Ideal: 3840x2160 (4K) para pantallas grandes")

                if bitrate < 8:
                    print(f"[!] Bitrate actual: {bitrate:.2f} Mbps")
                    print("  -> Se recomienda 8-12 Mbps para 1080p")
                    print("  -> Se recomienda 25-40 Mbps para 4K")

                print("\n[+] Para mejorar la calidad, re-encodear con:")
                print("  ffmpeg -i video_background.mp4 -c:v libx264 \\")
                print("         -preset slow -crf 18 \\")
                print("         -vf scale=1920:1080 \\")
                print("         -b:v 10M \\")
                print("         video_background_hq.mp4")
            else:
                print("[X] No se encontro stream de video")
        else:
            print("[X] ffprobe no disponible o error al ejecutar")
            print("   Instala FFmpeg para obtener informacion detallada")

    except FileNotFoundError:
        print("[X] ffprobe no esta instalado")
        print("\nPara obtener informacion detallada del video:")
        print("1. Descarga FFmpeg: https://ffmpeg.org/download.html")
        print("2. Anadelo al PATH del sistema")
        print("3. Ejecuta este script nuevamente")

else:
    print(f"[X] Video no encontrado en: {video_path}")
