from moviepy.editor import *
from config import frame as frame_path, audiofile, logo as logo_path


def edit_video(video_path):
    # Carrega o vídeo
    clip = VideoFileClip(video_path)

    # 1. Verificar e ajustar o tamanho do vídeo
    if clip.size != [724, 1282]:
        clip = clip.resize((724, 1282))

    # 2. Criar um canvas 1080x1920 (fundo preto)
    canvas = ColorClip(size=(1080, 1920), color=(
        0, 0, 0)).set_duration(clip.duration)

    # 3. Centralizar o vídeo no canvas
    video_on_canvas = CompositeVideoClip([canvas, clip.set_position("center")])

    # 4. Sobrepor a moldura
    frame = ImageClip(frame_path).set_duration(clip.duration)
    final_clip = CompositeVideoClip(
        [video_on_canvas, frame.set_position("center")])

    return final_clip


clip = VideoFileClip(video_path)
    video_clip.fps = clip.fps

def finalize_video(video_clip):
    # 5. Adicionar música ao vídeo

    # Extrair o áudio original do vídeo
    original_audio = video_clip.audio

    # Carregar a trilha sonora e ajustar o volume
    audio = AudioFileClip(audiofile)

    # Se o áudio for mais curto que o vídeo, repetir o áudio. Se for mais longo, cortá-lo.
    if audio.duration < video_clip.duration + 3:
        audio = audio.fx(vfx.loop, duration=video_clip.duration + 3)
    else:
        audio = audio.subclip(0, video_clip.duration + 3)

    # Ajustar o volume da trilha sonora para -15dB e diminuir nos últimos 3 segundos para -21dB
    audio = audio.volumex(0.15).fx(afx.audio_fadeout, 3).volumex(0.7)

    # Combinar o áudio original com a trilha sonora
    combined_audio = CompositeAudioClip([original_audio, audio])

    video_clip = video_clip.set_audio(combined_audio)

    # 6. Adicionar 3 segundos no final com o logo
    logo_clip = ImageClip(logo_path).set_duration(3)
    video_clip = concatenate_videoclips([video_clip, logo_clip])

    # 7. Exportar
    video_clip.write_videofile(
        "static/render/comunicado-renova.mp4", codec="libx264", audio_codec="aac")
