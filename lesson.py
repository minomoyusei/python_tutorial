x = {'a':1}
y = x
y['a'] = 1000
print(x)
print(y)
print(id(x))
print(id(y))

x = {'a':1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)
print(id(x))
print(id(y))