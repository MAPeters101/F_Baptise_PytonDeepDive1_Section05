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




