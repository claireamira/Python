from bs4 import BeautifulSoup
import requests

url = "https://www.hubertiming.com/home"
response = requests.get(url)

content = BeautifulSoup(response.content, "html.parser")

f = open("textFiles\web.html", "w")
f.write(str(content))

link_tags = content.find_all("a")

#for all in link_tags:
#    print(link.get("href"))

