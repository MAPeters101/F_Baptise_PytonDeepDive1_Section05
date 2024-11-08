def func1(a, b, c):
    print(a, b, c)

func1(1, 2, 3)
func1(1, c=3, b=2)

def func2(a, b, *args):
    print(a, b, args)

func2(1, 2, 3, 4)

def func3(a, b, *args, d):
    print(a, b, args, d)

#func3(1, 2, 3, 4, 5)
func3(1, 2, 3, 4, d=5)

def func3(*args, d):
    print(args, d)

func3(1, 2, 3, d='a')
func3(d='a')

def func4(*, d):
    print(d)

#func4(1, 2, d=100)
func4(d=100)

