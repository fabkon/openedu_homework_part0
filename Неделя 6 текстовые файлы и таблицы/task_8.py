fin = open("input.csv", "r", encoding="utf8")
fout = open("output.txt", "w", encoding="utf8")



zp = {}

for line in fin:
    now = line.split(';')
    if now[0] not in zp:
        zp[now[0]] = [1, int(now[1])]
    else:
        zp[now[0]][0] += 1
        zp[now[0]][1] += int(now[1])

sredn_zp = []
for company in zp:
    temp = (zp[company][1] / zp[company][0], company)
    sredn_zp.append(temp)

sredn_zp.sort()
for i in sredn_zp:
    print(i[1], file=fout)


#sort_list = sorted(sort_list, key=key_qnt, reverse=True)



fin.close()
fout.close()