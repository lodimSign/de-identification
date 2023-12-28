import os
import subprocess

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def send_slack_message(api_token, channel, message):
    client = WebClient(token=api_token)

    try:
        response = client.chat_postMessage(channel=channel, text=message)
        return response["ts"]  # 메시지의 timestamp 반환
    except SlackApiError as e:
        print(f"Error sending message to Slack: {e.response['error']}")

def check_slack_response(api_token, channel, timestamp):
    client = WebClient(token=api_token)

    try:
        response = client.conversations_replies(channel=channel, ts=timestamp)
        if response["messages"]:
            return True
        else:
            return False
    except SlackApiError as e:
        print(f"Error checking Slack response: {e.response['error']}")

def execute_and_shutdown(command, api_token, channel, completion_message):
    # 파일 실행
    subprocess.run(command, shell=True)

    # Slack으로 완료 메시지 전송
    completion_timestamp = send_slack_message(api_token, channel, completion_message)

    # Slack에서 응답 확인 후 컴퓨터 종료
    while not check_slack_response(api_token, channel, completion_timestamp):
        pass  # Slack에서 응답이 올 때까지 대기

    os.system("shutdown /s /t 1")  # /s: 종료, /t: 대기 시간 (초)

# Slack API 토큰과 메시지를 설정
slack_api_token = "xoxb-3465136584194-6270980115747-TKmpatWC1PN4H372xq8ei78l"
slack_channel = "C067C5J366T"
completion_message = "파일 실행이 완료되었습니다. 컴퓨터를 종료합니다."

# 파일 실행할 명령을 여기에 입력
file_command = "python your_script.py"

# 파일 실행 후 Slack 메시지 전송 및 컴퓨터 종료
execute_and_shutdown(file_command, slack_api_token, slack_channel, completion_message)