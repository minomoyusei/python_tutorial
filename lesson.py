print('hello')
print("hello")

print("I don't know")
print('I don\'t know')

print('say "I don\'t know"')
print("say \"I don't know\"")

print('hello. How are you?')
print('hello.\nHow are you?')

print('C:\\name\\name')

print('################')
print("""
line1
line2
line3
""")
print('################')

print('################')
print("""\
line1
line2
line3\
""")
print('################')

print('HI.' * 3 + 'Mike.')
s = ('aaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbb') #長い文章の時は''を2つ使う場合がある
print(s)

word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print(word[:])
print(word[:2])
print(word[2:])
word = 'j' + word[1:]
print(word)
n = len(word)
print(n)