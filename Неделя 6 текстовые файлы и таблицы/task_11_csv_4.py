fin = open("input.csv", "r", encoding="utf8")

food = fin.readline().strip().split(";")
print(food)

malls = fin.readlines()
prices=[]

for mall in malls:
    temp = mall.split(';')
    for i in range(len(temp)-1):
        prices.append((int(temp[i+1]), food[i+1], temp[0]))

prices.sort()
print(*prices[0][1:], sep='\n')

fin.close()
