from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

my_file = open('output.txt', 'w', encoding="utf8")


def my_funk(in_link):
    resp = urlopen(in_link) # скачиваем файл
    html = resp.read().decode('utf8') # считываем содержимое
    soup = BeautifulSoup(html, 'html.parser') # делаем суп
    q=set() #переменная подсчета
    m=0
    for x in soup.find_all('td'):
        print(x.text)
        m += int(x.text)
    return m

link_1 = 'https://stepik.org/media/attachments/lesson/209723/4.html'

print(my_funk(link_1), file=my_file)



my_file.close()