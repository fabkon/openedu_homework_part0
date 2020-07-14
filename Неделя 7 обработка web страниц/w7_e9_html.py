from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

my_file = open('output.txt', 'w', encoding="utf8")

resp = urlopen('https://stepik.org/media/attachments/lesson/209719/2.html') # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп


table = soup.find('code')
my_slovar={}
for prog in soup.find_all('code'):
    my_slovar[prog.text] = my_slovar.get(prog.text, 0) + 1
#    print(my_slovar.get(prog.text, 0))
'''    
    if prog.text not in my_slovar:
        my_slovar[prog.text] = 0
    my_slovar[prog.text] += 1
'''

print(max(my_slovar.values()))

my_list = []
for code in my_slovar:
    my_list.append((my_slovar[code], code))

my_list.sort()
for item in my_list:
    if item[0] == max(my_list)[0]:
        print(item[1], file=my_file, end=' ')
'''    
    if link.has_attr('href'):
        if link.get('href').startswith('http'):
            print(link.get('href'), file=my_file)
'''


my_file.close()