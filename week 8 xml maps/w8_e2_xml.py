from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

my_file = open('output.csv', 'w', encoding="utf8")


def my_funk(in_link): # находит таблицы с атриботом wikitable collapsible collapsed

    resp = urlopen(in_link) # скачиваем файл
    html = resp.read().decode('utf8') # считываем содержимое
    soup = BeautifulSoup(html, 'html.parser') # делаем суп
    table = soup.find_all('table', attrs={'class': 'wikitable collapsible collapsed'})
    return table

def new_csv (tables, i): #переводит таблицу html в список строк, где вложенные списки - стообцы, i - порядковый номер таблицы в супе table
    new_table = []
    for line in tables[i].find_all("tr"):
        temp = []
        for cell in line.find_all(["th", "td"]):
            temp.append(cell.text.strip())
        new_table.append(temp)
    return new_table

link_1 = 'https://stepik.org/media/attachments/lesson/258944/New-York.html'

work_table = my_funk(link_1)

for number_of_table in range(3):
    #print("--------------", number_of_table, file=my_file)
    table_csv = new_csv(work_table, number_of_table)
    #print(table_csv, file=my_file)
    for lines in table_csv:
        print(*lines, sep=',', end='\n', file=my_file)
    print(file=my_file)

my_file.close()