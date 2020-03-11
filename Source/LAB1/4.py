import requests
from bs4 import BeautifulSoup

URL = 'https://catalog.umkc.edu/course-offerings/graduate/comp-sci/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
myTitles = soup.find_all("span", class_="title")
myDesc = soup.find_all("p", class_="courseblockdesc")

print("number fo records fetched: " )
print("Titles: ", myTitles.__len__())
print("Descriptions: ", myDesc.__len__())
print("Records: ")
print("")
for elements in range(0, len(myTitles)):
    print(elements + 1)
    print(myTitles[elements].text)
    print(myDesc[elements].text)
    print("_" * 50)
