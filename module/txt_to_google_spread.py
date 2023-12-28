import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets API에 접근하기 위한 인증 설정
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(credentials)

# 스프레드시트의 이름이나 URL을 사용하여 열기
spreadsheet = client.open("Your Spreadsheet Name")

# 특정 워크시트 선택
worksheet = spreadsheet.get_worksheet(0)

# 텍스트 파일 읽기
with open("your_text_file.txt", "r") as file:
    lines = file.readlines()

# 데이터 추출 및 Google Sheets에 입력
for line in lines:
    if "count_box_total" in line:
        key, value = line.strip().split(":")
        key = key.strip()
        value = int(value.strip())
        # A열에 key, B열에 value를 추가
        worksheet.append_row([key, value])

print("Data has been successfully written to Google Sheets.")
