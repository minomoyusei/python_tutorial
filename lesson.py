d = {'x':10, 'y': 20}
print(d)
print(type(d))
print(d['x'])
d['x'] = 100
print(d['x'])
d['x'] = 'XXXX'
print(d)
d['z'] = 200
print(d)
d[1] = 10000
print(d)
print(dict(a=10,b=20))
dict([('a',10),('b',20)])