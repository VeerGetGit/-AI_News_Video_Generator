import requests
import os
import re

PEXELS_API_KEY = "YOUR_PEXELS_API_KEY"
HEADERS = {"Authorization": PEXELS_API_KEY}


def sanitize_filename(name):
    
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    name = re.sub(r"[^\x00-\x7F]+", "", name)
    name = name.replace(" ", "_")
    return name.lower()


def fetch_videos(keywords, num_videos=3):
    downloaded = []

    for keyword in keywords[:num_videos]:
        safe_keyword = sanitize_filename(keyword)
        clip_file = f"{safe_keyword}.mp4"
        clip_file = os.path.abspath(clip_file)  

        url = f"https://api.pexels.com/videos/search?query={keyword}&per_page=1"
        response = requests.get(url, headers=HEADERS)
        data = response.json()

        if not data.get("videos"):
            print(f"No video found for keyword: {keyword}")
            continue

        video_url = data["videos"][0]["video_files"][0]["link"]
        download_file(video_url, clip_file)
        downloaded.append(clip_file)

    return downloaded


def download_file(url, output_file):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(output_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded video: {output_file}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")
