import os
import whisper


FFMPEG_PATH = r"C:\Users\HVS\Downloads\gen ai news tool\ffmpeg\bin\ffmpeg.exe"

if not os.path.isfile(FFMPEG_PATH):
    raise FileNotFoundError(f"FFmpeg executable not found at: {FFMPEG_PATH}")

print(f" FFmpeg executable found at: {FFMPEG_PATH}")


os.environ["PATH"] += os.pathsep + os.path.dirname(FFMPEG_PATH)
os.environ["IMAGEIO_FFMPEG_EXE"] = FFMPEG_PATH

def generate_captions(audio_file="audio.mp3", output_srt="captions.srt"):
    if not os.path.isfile(audio_file):
        raise FileNotFoundError(f"Audio file not found: {audio_file}")

    print("Loading Whisper model...")
    model = whisper.load_model("base")

    print("Transcribing audio...")
    result = model.transcribe(audio_file)

    def fmt(t):
        h = int(t // 3600)
        m = int((t % 3600) // 60)
        s = t % 60
        ms = int((s - int(s)) * 1000)
        return f"{h:02}:{m:02}:{int(s):02},{ms:03}"

    with open(output_srt, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result.get("segments", []), start=1):
            start = fmt(segment["start"])
            end = fmt(segment["end"])
            text = segment["text"].strip()
            f.write(f"{i}\n{start} --> {end}\n{text}\n\n")

    print("Captions saved:", output_srt)
