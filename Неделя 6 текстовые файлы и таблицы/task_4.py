fin = open("input.txt", "r", encoding="utf8")
fout = open("output.txt", "w", encoding="utf8")

s = fin.readlines()

for i in s[::-1]:
    print(i, file=fout, end='')
#print(*s[::-1], end='', sep='')
fin.close()
fout.close()

