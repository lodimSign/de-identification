import requests
import json


def noti_slack():
    # Slack Incoming Webhook URL
    webhook_url = "https://hooks.slack.com/services/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"

    # 보낼 메시지
    message = {
        "text": "파이썬 파일 실행 완료.",
        "username": "PythonBot",
        "icon_emoji": ":snake:",  # 이모지는 원하는 것으로 변경 가능
    }

    # 메시지를 JSON 형식으로 변환하여 전송
    response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})

    # 응답 확인
    if response.status_code == 200:
        print("메시지 전송 성공")
    else:
        print(f"오류 발생: {response.status_code}")
        print(response.text)