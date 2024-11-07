a, b, *c = 10, 20, 'a', 'b'
print(a)
print(b)
print(c)
print()

def func1(a, b, *c):
    print(a)
    print(b)
    print(c)

func1(10, 20)
func1(10, 20, 1, 2, 3)
print()

def func2(a, b, *args):
    print(a)
    print(b)
    print(args)

func2(10, 20)
func2(10, 20, 1, 2, 3)
print()

def avg1(*args):
    print(args)

avg1()
print()

avg1(10, 20)
print()

def avg(*args):
    count = len(args)
    total = sum(args)
    return count and total/count
    # if count == 0:
    #     return 0
    # else:
    #     return total/count

print(avg(2, 2, 4, 4))
print()

print(avg())
print()

def avg2(a, *args):
    count = len(args) + 1
    total = sum(args) +a
    return total/count

print(avg2(2, 2, 4, 4))
print()

# print(avg2())
# print()


def func2(a, b, c):
    print(a)
    print(b)
    print(c)

l = [10, 20, 30]
#func2(l)
func2(l, 'x', 'y')
func2(*l)

print('-'*30)
l = [10, 20, 30, 40]
#func2(*l)
print()

def func3(a, b, c, *args):
    print(a)
    print(b)
    print(c)
    print(args)

l = [10, 20, 30, 40, 50]
func3(*l)



