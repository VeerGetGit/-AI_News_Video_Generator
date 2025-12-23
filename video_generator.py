import os
import time
import httpx
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
ACCESS_KEY = os.getenv("KLING_ACCESS_KEY", "").strip()
SECRET_KEY = os.getenv("KLING_SECRET_KEY", "").strip()

API_URL = "https://api.302.ai/klingai/v1/videos/text2video"
os.makedirs("output_videos", exist_ok=True)

def text_to_video(prompt_text, output_path="output_videos/video.mp4", duration=10,
                  model_name="kling-v2-master", sound="off", aspect_ratio="16:9"):
    """
    Generate a video from text using Kling API.
    """
    headers = {
        "Content-Type": "application/json",
        "Access-Key": ACCESS_KEY,
        "Secret-Key": SECRET_KEY
    }

    payload = {
        "prompt": prompt_text,
        "model_name": model_name,
        "duration": duration,
        "sound": sound,
        "aspect_ratio": aspect_ratio
    }

    # 1️⃣ Create a video generation task
    response = httpx.post(API_URL, headers=headers, json=payload, timeout=120)
    if response.status_code != 200:
        raise Exception(f"Kling API Error {response.status_code}: {response.text}")

    task_id = response.json()["data"]["task_id"]
    print(f"Task submitted: {task_id}")

    # 2️⃣ Poll the task until it succeeds or fails
    while True:
        status_resp = httpx.get(f"{API_URL}/{task_id}", headers=headers)
        status_data = status_resp.json()["data"]
        status = status_data.get("task_status")
        print(f"Current status: {status}")

        if status == "succeed":
            video_url = status_data["task_result"]["videos"][0]["url"]
            break
        elif status == "failed":
            raise Exception(f"Video generation failed: {status_data}")
        
        time.sleep(5)  # wait 5 seconds before polling again

    # 3️⃣ Download the generated video
    video_bytes = httpx.get(video_url).content
    with open(output_path, "wb") as f:
        f.write(video_bytes)
    
    print(f"Video saved to {output_path}")
    return output_path
