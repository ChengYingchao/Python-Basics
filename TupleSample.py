schoolmates = ('Jim','Aaron','Tim')
print(schoolmates)
print('第一位校友是',schoolmates[0])
T = ()
print('元组T的长度是',len(T))
#S = (5)
#print(S)
#print('元组S的长度是',len(S))
S = (5,)
print(S)
print('元组S的长度是',len(S))

roommates =  ('Jim','Aaron','Tim',['Tom','Jenny'])
print(roommates)
print('元组roommates的长度是',len(roommates))
print(roommates[3][0])
roommates[3][0] = 'Justin'
print(roommates)
L = [
    ['Apple','Google','Microsoft'],
    ['Java','python','ruby','php'],
    ['adam','bart','lisa']
]
print(L)
print('list列表L有',len(L),'个元素')
print(L[0][0])
print(L[1][0])
print(L[2][0])
print('请用列表list下标的形式打印出Google ruby 和 lisa：')
