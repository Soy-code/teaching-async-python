# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# pip install beautifulsoup4

"""
웹 크롤링 : 검색 엔진의 구축 등을 위하여 특정한 방법으로 웹 페이지를 수집하는 프로그램
웹 스크래핑 : 웹에서 데이터를 수집하는 프로그램
"""

from bs4 import BeautifulSoup

# html을 아래와 같이 가져올 것임
# 아래는 예시
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, "html.parser")

print("PRETTIFY:::")
print(soup.prettify())

print("TITLE:::")
print(soup.title)

# p tag
print("P:::")
print(soup.p)

print("FIND P AND TITLE:::")
print(soup.find("p", "title"))

print("FIND P AND STORY:::")
print(soup.find("p", "story"))
