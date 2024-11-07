l = [1, 2, 3, 4, 5, 6]

a = l[0]
b = l[1:]
print(a)
print(b)
print()

a, b = l[0], l[1:]
print(a)
print(b)
print()

a, *b = l
print(a)
print(b)
print()

# s = {1, 2, 3}
# a = s[0]
# b = s[1:]
# print(a)
# print(b)
# print()

s = {1, 2, 3}
a, *b = s
print(a)
print(b)
print()

s = 'python'
a, *b = s
print(a)
print(b)
print()

t = ('a', 'b', 'c')
a, *b = t
print(a)
print(b)
print()

[a, b, c] = ('XYZ')
print(a)
print(b)
print(c)
print()

a, b, *c = 'python'
print(a)
print(b)
print(c)
print()

a, b, *c, d = 'python'
print(a)
print(b)
print(c)
print(d)
print()

s = 'python'
a, b, c, d = s[0], s[1], s[2:-1], s[-1]
print(a)
print(b)
print(c)
print(d)
print()

s = 'python'
a, b, c, d = s[0], s[1], s[2:-1], s[-1]
*c, = c
print(a)
print(b)
print(c)
print(d)
print()

s = 'python'
a, b, c, d = s[0], s[1], s[2:-1], s[-1]
print(a)
print(b)
print(list(c))
print(d)
print()
print('='*30)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]
print(l)
print()

l1 = [1, 2, 3]
s = 'abc'
l = [*l1, *s]
print(l)
print()

l1 = [1, 2, 3]
s = {'x', 'y', 'z'}
l = [*l1, *s]
print(l)
print()

s1 = 'abc'
s2 = 'cde'
l = [*s1, *s2]
print(l)
print()

s1 = 'abc'
s2 = 'cde'
s = {*s1, *s2}
print(s)
print()

s = {10, -99, 3, 'd'}
for c in s:
    print(c)
a, b, c, d = s
print(a)
print(b)
print(c)
print(d)
print()

s = {10, -99, 3, 'd'}
a, b, *c = s
print(a)
print(b)
print(c)
print()

s = {10, -99, 3, 'd'}
print(list(s))
*c, = s
print(c)
print()
print('+'*30)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
#s = s1 + s2
s = {*s1, *s2}
print(s)
print()

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s = s1.union(s2)
print(s)
print()

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
s4 = {7, 8, 9}
s = s1.union(s2).union(s3).union(s4)
print(s)
print()

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
s4 = {7, 8, 9}
s = s1.union(s2, s3, s4)
print(s)
print()

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
s4 = {7, 8, 9}
s = {*s1, *s2, *s3, *s4}
print(s)
l = [*s1, *s2, *s3, *s4]
print(l)
print()


d1 = {'key1': 1, 'key2': 2}
d2 = {'key2': 3, 'key4': 4}
d = {*d1, *d2}
print(d)
d = {**d1, **d2}
print(d)
d = {**d2, **d1}
print(d)
print()







