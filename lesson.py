d = {'x': 10, 'y': 20}
help(d)
print(d.keys())
print(d.values())
d2 = {'x': 1000, 'j': 500}
print(d)
print(d2)
d.update(d2)
print(d)
print(d['x'])
print(d.get('x'))
print(d.get('z'))
r = d.get('z')
print(r)
print(type(r))
print(d.pop('x'))
print(d)
del d['y']
print(d)
del d
d = {'a': 100, 'b': 200}
d.clear()
print(d)
d = {'a': 100, 'b': 200}
print('a' in d)