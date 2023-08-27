i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j = ', j)
print('i = ', i)


x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('y = ', y)
print('x = ', x)

X = 10
Y = X
print(id(Y))
Y = 5
print(Y)
print(X)
print(id(X))
print(id(Y))

X = ['a', 'b']
Y = X
Y[0] = 'p'
print(id(X))
print(id(Y))
print(Y)
print(X)
