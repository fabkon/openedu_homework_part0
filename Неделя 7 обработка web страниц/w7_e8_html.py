from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

my_file = open('out_put.txt', 'w', encoding="utf8")

resp = urlopen('https://stepik.org/media/attachments/lesson/258939/webpage.html') # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп
table = soup.find('table', attrs = {'class' : 'wikitable sortable'})
for link in soup.find_all('a'):
    if link.has_attr('href'):
        if link.get('href').startswith('http'):
            print(link.get('href'), file=my_file)

my_file.close()