# https://ocr.space/OCRAPI
import requests
import json
# url = "https://api.ocr.space/parse/imageurl?apikey=입력할 api 키&url=넣을 이미지의 url&language=kor&isOverlayRequired=true"

def ocr(address : str =''):
    url = f"https://api.ocr.space/parse/imageurl?apikey=K89684037288957&url= {address} &language=kor&isOverlayRequired=true"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    response.raise_for_status()

    print(json.dumps(data, ensure_ascii=False, indent=2))

# print(data['ParsedResults'][0]['ParsedText'])