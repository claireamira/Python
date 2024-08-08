from bs4 import BeautifulSoup
import requests
import re

url = "https://www.safaricom.co.ke/home"
response = requests.get(url)

content = BeautifulSoup(response.content, "html.parser")

f = open("textFiles\web2.html", "w")
f.write(str(content))

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content.text)
print("Emails :", emails)

phone_numbers = re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', content.text)
print("Phone numbers :", phone_numbers)