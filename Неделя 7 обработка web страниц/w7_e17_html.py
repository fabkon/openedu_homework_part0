from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

my_file = open('output.txt', 'w', encoding="utf8")


def my_funk(in_link):
    resp = urlopen(in_link) # скачиваем файл
    html = resp.read().decode('utf8') # считываем содержимое
    soup = BeautifulSoup(html, 'html.parser') # делаем суп
    table = soup.find_all('table', attrs={'class': 'wikitable collapsible collapsed'})
    return table[1]


link_1 = 'https://stepik.org/media/attachments/lesson/258944/New-York.html'

print(my_funk(link_1), file=my_file)

my_file.close()