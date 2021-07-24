from random import randint

N = 10
a = [randint(-100, 100) for j in range(N)]
print(*a)

for i in range(N-1, -1, -1):
    if -50 < a[i] < 50:
        del a[i]
    i -= 1


print(*a)




















users1 = ["Mike", "Jimmy", "Jeremy"]
users2 = users1
users2.append("Carl")
print(users1)
print(users2)



















a = [5, [1,2], 2, 'r', 4, 'ee', 'ee']
b = [4, 'we', 'ee', 3, [1, 2]]
c = []
for i in a:
    if i in c:
        continue
    for j in b:
        if i ==j:
            c.append(i)
            break


print(c)




















dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic4={}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)



















d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)