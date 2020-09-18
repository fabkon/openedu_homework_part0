from urllib.request import urlopen

my_url = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html")
html = my_url.read().decode("utf-8").split()

c = 0
p = 0
for word in html:
    if "C++" in word:
        c += 1
    if "Python" in word:
        p +=1

if c>p:
    print("C++")
else:
    print("Python")

