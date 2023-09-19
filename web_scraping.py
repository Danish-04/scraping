
from bs4 import BeautifulSoup
import requests

url="https://www.tech2secure.com/"
response=requests.get("https://www.tech2secure.com/")
html=response.text


soup= BeautifulSoup(html,"html.parser")
headings=soup.find_all(["h1","h2","h3"])
para=soup.find_all(["p"])

for heading in headings :
    print(heading.text)


