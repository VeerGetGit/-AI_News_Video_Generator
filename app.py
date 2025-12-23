import asyncio
import os
from scraped_news import scrape_google_top_news
from script_generator import generate_script
from tts_audio import generate_audio
from captions import generate_captions
from pexels import fetch_videos
from stitcher import create_video

def main():
    # 1️⃣ Scrape news
    articles = scrape_google_top_news(num_articles=1)
    if not articles:
        print("No news articles found. Exiting...")
        return

    news = articles[0]
    # Ensure summary key exists
    news_summary = news.get("summary", "")
    topic_summary = f"{news['title']}. {news_summary}"
    print("News scraped:", news['title'])

    # 2️⃣ Generate narration & keywords
    script_data = generate_script(topic_summary)
    narration_text = script_data.get("narration", topic_summary)
    visual_keywords = script_data.get("visual_keywords", ["news", "headlines"])

    print("Narration for TTS:\n", narration_text)
    print("Visual keywords:", visual_keywords)

    
    audio_path = os.path.abspath("audio.mp3")
    asyncio.run(generate_audio(narration_text, output_file=audio_path))

    
    captions_path = os.path.abspath("captions.srt")
    generate_captions(audio_file=audio_path, output_srt=captions_path)

    
    cleaned_keywords = [k for k in visual_keywords if len(k.split()) <= 3 and k.isascii()]
    clips = fetch_videos(cleaned_keywords, num_videos=2)
    if not clips:
        print("No video clips fetched. Exiting...")
        return
    clips = [os.path.abspath(c) for c in clips]
    print("Fetched video clips:", clips)

    
    final_video_path = os.path.abspath("final_video.mp4")
    
    create_video(
        clips,
        audio_file=audio_path,
        output_file=final_video_path
    )
    print("🎬 Final video generated:", final_video_path)


if __name__ == "__main__":
    main()
