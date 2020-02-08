import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Deep_learning'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.title.string)

for link in soup.find_all('a'):
    print(link.get('href'))

#
# Write a simple program that parse a Wiki page
# mentioned below and follow the instructions:
# https://en.wikipedia.org/wiki/Deep_learnisng
# a. Print out the title of the page
# b. Find all the links in the page (‘a’ tag)
# c. Iterate over each tag(above) then return the link using attribute "href" using get
