my_web = open('my_html.html', 'w', encoding="utf8")

print("""

<html>
<body>

<table>
""", file=my_web)


for i in range(1, 11):
    print('<tr>', end='', file=my_web)
    for j in range(1, 11):
        print('<td> <a href=http://',i*j, '.ru>',i*j, '</a> </td>', file = my_web, sep='', end='')
    print('</tr>', file=my_web)

print("""
</table>
</body>
</html>
""", file=my_web)