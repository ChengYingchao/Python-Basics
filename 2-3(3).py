num1 = int(input("请输入第一个奇数："))
num2 = int(input("请输入第2个奇数："))
num3 = int(input("请输入第3个奇数："))
num4 = int(input("请输入第4个奇数："))
num5 = int(input("请输入第5个奇数："))
list001 = [num1,num2,num3,num4,num5]

print('刚才输入的奇数个数是：',len(list001),"组成的列表是：",list001)
list001.sort()
print('列表排序后是：',list001)
print('将奇数按降序排序输出:')
n = len(list001)-1
while list001:
    print(list001[n])
    list001.pop()
    n = n-1





