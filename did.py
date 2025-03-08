import requests
import time
from datetime import datetime
from config import D_ID_USERNAME, D_ID_PASSWORD
from config import source_image_url


BASE_URL = "https://api.d-id.com/talks"


def generate_video_from_text(source_image_url, text):
    payload = {
        "source_url": source_image_url,
        "config": {
            "stitch": True
        },
        "script": {
            "type": "text",
            "input": text,
            "provider": {
                "type": "microsoft",
                "voice_id": "pt-PT-FernandaNeural",
                "voice_config": {
                    "style": "Happy"
                }
            }
        }
    }
    response = requests.post(BASE_URL, json=payload,
                             auth=(D_ID_USERNAME, D_ID_PASSWORD))
    if response.status_code != 201:
        raise Exception(f"Failed to generate video: {response.text}")
    talk_id = response.json().get("id")
    return talk_id


def get_video_url(talk_id):
    url = f"{BASE_URL}/{talk_id}"
    response = requests.get(url, auth=(D_ID_USERNAME, D_ID_PASSWORD))
    if response.status_code != 200:
        raise Exception(f"Failed to fetch video: {response.text}")
    status = response.json().get("status")
    if status != "done":
        return None
    result_url = response.json().get("result_url")
    return result_url


def download_from_url(url: str) -> str:
    if not url:
        raise Exception("Invalid URL provided.")
    file_name = 'downloaded_video_' + datetime.now().strftime("%Y%m%d%H%M%S") + ".mp4"
    response = requests.get(url, stream=True)
    with open(file_name, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)
    return file_name


def create_and_download_video(source_image_url, text):
    talk_id = generate_video_from_text(source_image_url, text)
    video_url = None
    while not video_url:
        video_url = get_video_url(talk_id)
        if not video_url:
            time.sleep(10)
    downloaded_file = download_from_url(video_url)
    return downloaded_file
