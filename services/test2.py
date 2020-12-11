f = open('/home/aidar/PycharmProjects/pythonProject1/workbot/cities.txt', 'r')
city = input()
a = []
for i in f:
    i = i.replace('\n','')
    a.append(i)
k = 0
for i in a:
    if city == i.lower():
        k += 1
if k != 1:
    print('ты лох')
else:
    print('ты не лох')

f.close()