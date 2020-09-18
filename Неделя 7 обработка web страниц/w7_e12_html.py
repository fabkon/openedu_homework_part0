from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

my_file = open('output.txt', 'w', encoding="utf8")


def my_funk(in_link):
    resp = urlopen(in_link) # скачиваем файл
    html = resp.read().decode('utf8') # считываем содержимое
    soup = BeautifulSoup(html, 'html.parser') # делаем суп
    exc = ['http', '#', '//'] #исключения для подсчета
    q=set() #переменная подсчета
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            temp = True
            for i in exc:
                if link.get('href').startswith(i):
                    temp = False
            if temp and (':' not in link.get('href')):
                q.add(link.get('href'))
    print(q)
    print(len(q))
    return q

link_1 = 'https://stepik.org/media/attachments/lesson/258943/Moscow.html'
link_2 = 'https://stepik.org/media/attachments/lesson/258944/New-York.html'

print(len(my_funk(link_1) & my_funk(link_2)), file=my_file)
print(len)
#table = soup.find('table', attrs = {'class' : 'wikitable sortable'})

my_file.close()