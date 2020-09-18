fin = open("input.csv", "r", encoding="utf8")
fout = open("output.txt", "w", encoding="utf8")



for line in fin:
    temp1 = line.split(';')
    print(int(temp1[1]), temp1[0], sep=";", end="\n", file=fout)



fin.close()
fout.close()