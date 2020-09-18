fin = open("input.txt", "r", encoding="utf8")
fout = open("output.txt", "w", encoding="utf8")


lines= fin.readlines()
line_length = 0
for line in lines:
    if line_length < len(line):
        line_length = len(line)

for line in lines:
    if line_length == len(line):
        print(line)




#print(, file=fout)

fin.close()
fout.close()