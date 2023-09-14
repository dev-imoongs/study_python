# https://developers.naver.com/docs/papago/papago-nmt-overview.md
# YOUR_CLIENT_ID = oiKTtsHyWl6Sf7QKIgvd
# YOUR_CLIENT_SECRET = _0jGWc_AvV



import os
import sys
import urllib.request
import json
def from_ko_to_en(text : str):
    client_id = "oiKTtsHyWl6Sf7QKIgvd" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "_0jGWc_AvV" # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(text)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        # print(type(response_body.decode('utf-8'))) # json 형식이라 str 반환
        # print(json.loads(response_body.decode('utf-8')))
        # print(type(json.loads(response_body.decode('utf-8')))) # loads 사용하여 dict로 변환
        # # dict안에 값 추출
        # print(json.loads(response_body.decode('utf-8'))["message"]["result"]["translatedText"])
    else:
        print("Error Code:" + rescode)

    return json.loads(response_body.decode('utf-8'))["message"]["result"]["translatedText"]