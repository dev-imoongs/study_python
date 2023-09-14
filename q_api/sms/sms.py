import json
import platform
import requests
import q_api.sms.config as config
import q_api.sms.auth as auth

def send_sms(random_six: str = '000000'):
    default_agent = {
        'sdkVersion': 'python/4.2.0',
        'osPlatform': platform.platform() + " | " + platform.python_version()
    }


    url = "http://api.coolsms.co.kr/messages/v4/send"
    headers = auth.get_headers('NCSA2GEWYWJO2DRP', 'RPWN8MD9VMBXA6CNMYSLAOP0GL9JNU2L')

    data = {
        "message": {
            "to": "01029237309",
            "from": "01029237309",
            "text": random_six
        }
    }
    print(json.dumps(data, ensure_ascii=False))
    response = requests.post(config.get_url('/messages/v4/send'),
                             headers=auth.get_headers(config.api_key, config.api_secret),
                             json=data)
    print(response.status_code)
    print(response.text)
    return random_six
