# 네이버 블로그에서 검색어에 따른 상위 N개 게시글 정보 추출 (제목, 게시글 URL, 게시글 내용(약 100자), 블로그 이름, 블로그 URL, 작성일)
# 네이버 API 사용
import json
import os
import sys
import urllib.request

# config.json 데이터 불러오기
def load_config():
    base_dir = os.path.dirname(__file__)  # 현재 파일이 있는 경로 (c:\dev\crawling_upload_github\naver)
    config_path = os.path.join(base_dir, 'config.json') #        (c:\dev\crawling_upload_github\naver\config.json)
    with open(config_path, 'r', encoding='utf-8') as config_file:
        return json.load(config_file)
    
config = load_config()



# 네이버 검색 API 예제 - 블로그 검색
client_id = config["NAVER_API_client_id"]
client_secret = config["NAVER_API_client_secret"]
search = "삼성전자" # 검색어

encText = urllib.parse.quote(search)

url = "https://openapi.naver.com/v1/search/blog.json?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)