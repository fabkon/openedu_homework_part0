fin = open("input.txt", "r", encoding="utf8")
fout = open("output.txt", "w", encoding="utf8")
def key_qnt(x):
    return x[0]
def key_name(x):
    return x[1]

tes = fin.read().split()
words = {}
for word in tes:
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1
new_list = []
for word in words:
    temp = (words[word], word)
    new_list.append(temp)
sort_list = sorted(new_list, key=key_name)
sort_list = sorted(sort_list, key=key_qnt, reverse=True)

for i in sort_list:
    print(i[1], end=" ", file=fout)

fin.close()
fout.close()