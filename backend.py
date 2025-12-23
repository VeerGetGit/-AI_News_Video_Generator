from flask import Flask, request, jsonify
from scraped_news import scrape_google_top_news
from script_generator import generate_script
from tts_audio import generate_audio
from pexels import fetch_videos
from stitcher import create_video
import asyncio
import os

app = Flask(__name__)

@app.route("/generate_video", methods=["POST"])
def generate_video():
    try:
        
        num_articles = int(request.json.get("num_articles", 1))
        
       
        articles = scrape_google_top_news(num_articles=num_articles)
        if not articles:
            return jsonify({"error": "No news found"}), 404

        news = articles[0]
        topic_summary = f"{news['title']}. {news['summary']}"

        
        script_data = generate_script(topic_summary)
        narration_text = script_data["narration"]
        visual_keywords = script_data["visual_keywords"]

        
        audio_path = os.path.abspath("audio.mp3")
        asyncio.run(generate_audio(narration_text, output_file=audio_path))

        
        clips = fetch_videos(visual_keywords, num_videos=5)
        clips = [os.path.abspath(c) for c in clips if os.path.isfile(c)]
        if not clips:
            return jsonify({"error": "No video clips fetched"}), 404

        
        final_video_path = os.path.abspath("final_video.mp4")
        create_video(clips, audio_file=audio_path, output_file=final_video_path)

        return jsonify({"success": True, "video_path": final_video_path})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
