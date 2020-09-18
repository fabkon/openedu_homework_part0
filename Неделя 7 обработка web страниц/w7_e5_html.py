from urllib.request import urlopen
#from bs4 import BeautifulSoup

my_url = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html")
html = my_url.read().decode("utf-8")




print(html)