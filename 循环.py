names = ['Michael', 'Bob', 'Tracy']
print(names)
for name in names:
    print('hello',name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum +x
print(sum)
print(list(range(5)))

he = 0
m = 100
while m>=0:
    he = he + m
    m = m - 2
print(he)

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

p = 0
while p < 15:
    p = p+1
    if p % 2 == 0:
        continue
    print(p)

#q = 0
#while q < 1:
#    print("000")


