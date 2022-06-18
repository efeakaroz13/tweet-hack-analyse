import requests
from bs4 import BeautifulSoup

out =[]
nextlink = "https://nitter.net/search?f=tweets&q=%22hacking%22&f-safe=on&e-replies=on&since=&until=&near="
months = ['Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
s = requests.Session()
for i in range(10):
    page = s.get(nextlink)
    soup = BeautifulSoup(page.content,"html.parser")
    all_timeline_items = soup.find_all("div",{"class":"timeline-item"})
    nextlink = "https://nitter.net/search"+str(soup.find_all("a",string="Load more")[0].get("href"))


    for ti in all_timeline_items:
        try:
            username = ti.find_all("a",{"class":"username"})[0].get_text()
            date = ti.find_all("span",{"class":"tweet-date"})[0].get_text()
            content = ti.find_all("div",{"class":"tweet-content"})[0].get_text()
            cantadd = False
            for m in months:
                try:
                    date.split(m)[1]
                    cantadd=True
                    break
                except:
                    pass
            if cantadd == False:
                data={
                    "username":username,
                    "date":date,
                    "content":content

                }
                out.insert(0,data)

        except:
            pass
    print(len(out))
