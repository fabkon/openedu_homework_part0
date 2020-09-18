from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

my_file = open('output.txt', 'w', encoding="utf8")


def my_funk(in_link):
    resp = urlopen(in_link) # скачиваем файл
    html = resp.read().decode('utf8') # считываем содержимое
    soup = BeautifulSoup(html, 'html.parser') # делаем суп
    exc = ['http', '#', '//'] #исключения для подсчета
    q=0 #переменная подсчета
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            temp = True
            for i in exc:
                if link.get('href').startswith(i):
                    #print(i, link.get('href'))
                    temp = False
            if ':' not in link.get('href'):
                print(temp, link.get('href'))
            if temp and (':' not in link.get('href')):
                q += 1
                print(link.get('href'), file=my_file)
    return q

link_1 = 'https://stepik.org/media/attachments/lesson/258943/Moscow.html'
link_2 = 'https://stepik.org/media/attachments/lesson/258944/New-York.html'

print(my_funk(link_1), my_funk(link_2), file=my_file)

#table = soup.find('table', attrs = {'class' : 'wikitable sortable'})

my_file.close()