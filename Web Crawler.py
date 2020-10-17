import urllib.request as req
import json
import html

src = "https://www.ptt.cc/bbs/movie/index.html"

#建立一個request物件,附加 request header 的資訊
request = req.Request(src,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"})

with req.urlopen(request) as response:
    #data = json.load(response)
    data = response.read().decode("utf-8")
#解析原始碼
import bs4 
root = bs4.BeautifulSoup(data,"html.parser")
titles = root.find_all("div",class_="title")# 尋找 class = "title" 的 div 標籤
for tt in titles:  
  if tt.a != None:
    print(tt.a.string)
#將公司名稱列表出來
'''
clist = data["result"]["results"]
with open("test.txt",mode = "w") as file:

  for company in clist:
'''''