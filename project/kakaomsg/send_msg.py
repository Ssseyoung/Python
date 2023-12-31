import json
import requests

# access_token
access_token = '7FFzwG-arM0t97AHhMPoU29J3xPzbIZS-xVLTprzCj10mQAAAYjiI1fc'


url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'


# header 정보
headers = {
    'Authorization' : 'Bearer ' + '7FFzwG-arM0t97AHhMPoU29J3xPzbIZS-xVLTprzCj10mQAAAYjiI1fc'
}

# 요청 정보
temp = {
            # "object_type": "text",
            # "text": input('메시지 : '),
            # "link": {
            #     "web_url": "https://www.youtube.com",
            #     "mobile_web_url": "https://www.youtube.com"
            # },
            "object_type": "feed",
            "content" : {
                "title" : input("제목 : "),
                "description" : input("내용 : "),
                "image_url": input("img url : "),
                "image_width": 640,
                "image_height": 640,
                'link' : { 
                    "web_url" : 'https://youtube.com',          # PC 카톡의 URL
                    "mobile_web_url" : 'https://youtube.com'    # 모바일 URL
                }
            },
           "buttons" : [
                {
                    "title" : "바로 가기",
                    'link' : { 
                        "web_url" : 'https://youtube.com',          # PC 카톡의 URL
                        "mobile_web_url" : 'https://youtube.com'    # 모바일 URL
                    }
                }
            ]
            
        }

data = {
    'template_object' : json.dumps( temp )      # 파이썬 객체를 JSON 문자열로 직렬화하는 함수
}

# 나에게 카카오 메세지 보내기
response = requests.post(url, headers=headers, data=data)
print(response.status_code)

