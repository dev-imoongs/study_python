# https://ocr.space/OCRAPI
import requests
import json

url = "https://api.ocr.space/parse/imageurl?apikey=K84875884788957&url=https://i.pinimg.com/474x/34/8b/c5/348bc51a10af4a96dea207318f88cc6b.jpg&language=kor&isOverlayRequired=true"

response = requests.get(url)
response.raise_for_status()

data = response.json()
print(data['ParsedResults'][0]['ParsedText'])

# print(json.dumps(data, ensure_ascii=False, indent=2))