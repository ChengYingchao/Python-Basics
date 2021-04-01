d = {'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])

d['Adam'] = 67
print(d['Adam'])

d['Michael'] = 100
print(d['Michael'])
print(d)


print('Tim' in d )
print(d.get('Tim'))

d.pop('Bob')
print(d)

s = set([1, 1, 2, 2, 3, 3])
print(s)
s.add(4)
print(s)
s.add(4)
print(s)

s.remove(4)
print(s)



for name in d:
    print(name,"的分数是",d[name])
