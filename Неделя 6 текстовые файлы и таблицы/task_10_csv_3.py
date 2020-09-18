fin = open("input.csv", "r", encoding="utf8")


food = fin.readline().split(";")

malls = fin.readlines()

prices=[]

shops=[]
for mall in malls:
    temp = list(map(int, mall.split(";")[1:]))
    shops.append(temp)

for i in shops:
    prices.append([min(i), i.index(min(i))])
print(min(prices)[0])



fin.close()
