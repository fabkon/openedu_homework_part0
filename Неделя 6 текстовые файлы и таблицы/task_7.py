fin = open("input.txt", "r", encoding="utf8")
fout = open("output.txt", "w", encoding="utf8")


lines= fin.read()
print(lines[-1::-1], sep='', end='')



print(lines[::-1], sep='', end='', file=fout)

fin.close()
fout.close()