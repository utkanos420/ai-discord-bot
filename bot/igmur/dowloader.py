from configs.config import igmur_settings
import requests

def upload_image_to_imgur(image_path: str) -> str:

    client_id = igmur_settings.igmur_client_token
    url = "https://api.imgur.com/3/image"
    headers = {"Authorization": f"Client-ID {client_id}"}

    with open(image_path, "rb") as image_file:
        files = {"image": image_file}
        response = requests.post(url, headers=headers, files=files)
    
    if response.status_code == 200:
        return response.json()["data"]["link"]
    else:
        raise Exception(f"Error: {response.status_code} - {response.json()}")