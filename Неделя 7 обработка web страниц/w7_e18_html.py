from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

my_file = open('output.csv', 'w', encoding="utf8")


def my_funk(in_link):
    resp = urlopen(in_link) # скачиваем файл
    html = resp.read().decode('utf8') # считываем содержимое
    soup = BeautifulSoup(html, 'html.parser') # делаем суп
    table = soup.find_all('table', attrs={'class': 'wikitable collapsible collapsed'})
    new_table = []
    for line in table[1].find_all("tr"):
        temp = []
        for cell in line.find_all(["th", "td"]):
            temp.append(cell.text.strip())
        new_table.append(temp)
    return new_table


link_1 = 'https://stepik.org/media/attachments/lesson/258944/New-York.html'

for i in my_funk(link_1):
    print(*i, sep=',', end='\n', file=my_file)

my_file.close()