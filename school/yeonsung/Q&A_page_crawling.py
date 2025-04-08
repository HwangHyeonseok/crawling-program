# 연성대학교 Q&A 게시판 제목 키워드 분석
# 상업적 목적 이용 금지
# 상업적 이용 시 모든 법적 책임은 프로그램 사용자에게 있음을 명시합니다.

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from collections import Counter
import time

# 1. 제목 크롤링
driver = webdriver.Chrome()
url = "https://www.yeonsung.ac.kr/ko/631/subview.do"
driver.get(url)
time.sleep(2)

titles = []

current_page = 1
max_page = 30

while current_page <= max_page:
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    strongs = soup.select('td.td-subject strong')

    for tag in strongs:
        title = tag.get_text(strip=True)
        titles.append(title)

    try:
        if current_page % 10 == 0:
            next_btn = driver.find_element(By.CLASS_NAME, "_next")
            next_btn.click()
        else:
            next_btn = driver.find_element(By.LINK_TEXT, str(current_page + 1))
            next_btn.click()
    except Exception as e:
        print("페이지 이동 실패:", e)
        break

    current_page += 1

driver.quit()

# 2. 단어 빈도 분석
all_words = []

for title in titles:
    words = title.split()  # 공백 기준 나눔 (한글은 konlpy 쓰면 더 정교함)
    all_words.extend(words)

counter = Counter(all_words)

# 3. 결과 출력
print("\n📊 자주 등장한 키워드 TOP 20:")
for word, freq in counter.most_common(20):
    print(f"{word}: {freq}")