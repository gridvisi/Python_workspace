

import easygui
import requests
from selenium import webdriver

url = easygui.enterbox("Enter URL:")
print("Loading...")

link = []
print("Get HTML source...")

browser = webdriver.Chrome()
browser.delete_all_cookies()
browser.get(url)
print("Find Download URL...")

html = str(browser.page_source.encode("utf8")).split(' ')

for j in html:
    if j.count("src="):
        link.append(j)

dlurl = link[17][5:-1]
print("Starting Download Music...")

cache = requests.get(dlurl)
name = input("Enter Name:")

with open(name+".mp3", 'wb') as code:
    code.write(cache.content)

code.close()

print("Download Over")

from selenium import webdriver
import time

def main():
    b = webdriver.Chrome()
    b.get('https://www.baidu.com')
    time.sleep(5)
    b.quit()
if __name__ == '__main__':
    main()