a = (1, 2, 3)
print(type(a))
print(a)

a = 1, 2, 3
print(type(a))
print(a)

a = (1)
print(type(a))
print(a)

a = ('a')
print(type(a))
print(a)

a = (1,)
print(type(a))
print(a)

a = 100,
print(type(a))
print(a)

a = ()
print(type(a))
print(a)

# a = ,
# print(type(a))
# print(a)

# a = (,)
# print(type(a))
# print(a)
print('='*30)

a, b, c = [1, 'a', 3.14]
print(a)
print(b)
print(c)
print()

(a, b, c) = [1, 2, 3]
print(a)
print(b)
print(c)
print()

a, b = (1, 2)
print(a)
print(b)
print()

(a, b) = (1, 2)
print(a)
print(b)
print()

a, b = 10, 20
print(a)
print(b)
print()

a, b, c = 10, 'a', 3.14
print(a)
print(b)
print(c)
print()

a, b, c = 10, {1, 2}, ['a', 'b']
print(a)
print(b)
print(c)
print()

a, b = 10, 20
print(a)
print(b)
a, b = b, a
print(a)
print(b)
print()
print('+'*30)

for e in 'XYZ':
    print(e)
print()

a, b, c = 'XYZ'
print(a)
print(b)
print(c)
print()

s = 'XYZ'
print(s[0])
print(s[1])
print(s[2])
print()

s = {1, 2, 3}
# print(s[0])
# print(s[1])
# print(s[2])
print()

s = {'p', 'y', 't', 'h', 'o', 'n'}
print(s)
print()

for e in s:
    print(e)
print()

a,b,c,d,e,f = s
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print()

d = {'a':1, 'b':2, 'c':3}
for e in d:
    print(e)
print()

a,b,c = d
print(a)
print(b)
print(c)
print()

d = {'a':1, 'b':2, 'c':3, 'd':4}
for e in d:
    print(e)
print()

a,b,c,d = d
print(a)
print(b)
print(c)
print(d)
print()
print('-'*20)

d = {'a':1, 'b':2, 'c':3, 'd':4}
for e in d:
    print(e)
print()

d,a,b,c = d
print(a)
print(b)
print(c)
print(d)
print()

print('='*40)
d = {'a':1, 'b':2, 'c':3, 'd':4}
for e in d:
    print(e)
print()

for e in d.values():
    print(e)
print()

a,b,c,d = d.values()
print(a)
print(b)
print(c)
print(d)
print()

dict1 = {'a':1, 'b':2, 'c':3, 'd':4}
for e in dict1.items():
    print(e)
print()

for e in dict1.items():
    a, b = e
    print('key={0}, value={1}'.format(a, b))
print()

for a, b in dict1.items():
    print('key={0}, value={1}'.format(a, b))
print()



