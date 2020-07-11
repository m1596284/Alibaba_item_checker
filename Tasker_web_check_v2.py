import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import re
pyPath, filename = os.path.split(__file__)
# Run on Tasker'
Main_page = "https://shop62s5a9474h055.1688.com/page/offerlist.htm?suggestiontype=winport&spm=a2615.2177701.20151125147.d147&keywords="
Book =[]

f = open(pyPath + "/A.txt","r", encoding='UTF-8')
readFile = f.readlines()
f.close
keyword = "抱歉，没有找到符合条件的供应信息。请重新搜索"

for url in range(0,len(readFile)):
    r=requests.get(Main_page + readFile[url].strip('\n'))
    print(r.text.find(keyword))
    Book.append(r.text.find(keyword))

f = open(pyPath + "/AB.txt","w", encoding='UTF-8')
for YN in Book:
    f.write(str(YN) + '\n')
f.close