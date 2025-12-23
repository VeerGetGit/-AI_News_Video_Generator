import os
import subprocess
import random
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip


DEFAULT_FFMPEG_PATHS = [
    r"C:\ffmpeg\bin\ffmpeg.exe",
    r"C:\Users\HVS\Downloads\gen ai news tool\ffmpeg\bin\ffmpeg.exe"
]

FFMPEG_PATH = None
for path in DEFAULT_FFMPEG_PATHS:
    if os.path.isfile(path):
        FFMPEG_PATH = path
        break

if not FFMPEG_PATH:
    raise FileNotFoundError(" FFmpeg executable not found. Please install FFmpeg and set path.")
else:
    print(f" FFmpeg executable found at: {FFMPEG_PATH}")
    os.environ["IMAGEIO_FFMPEG_EXE"] = FFMPEG_PATH


def create_video(clips, audio_file="audio.mp3", output_file="final_video.mp4"):
    """
    Combine clips with audio, no subtitles, and shuffle clips for variation.
    """
    if not clips:
        raise ValueError("No video clips provided!")
    random.shuffle(clips)

    
    video_clips = [VideoFileClip(os.path.abspath(c)) for c in clips]
    final_clip = concatenate_videoclips(video_clips, method="compose")

    
    audio = AudioFileClip(os.path.abspath(audio_file))
    final_clip = final_clip.set_audio(audio)

    
    final_clip.write_videofile(output_file, fps=24, codec="libx264", audio_codec="aac")

    
    final_clip.close()
    audio.close()
    for clip in video_clips:
        clip.close()

    print(f"🎬 Final video saved: {output_file}")
