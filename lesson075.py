def func1(a, b, *args):
    print(a, b, args)

func1(1, 2, 'x', 'y', 'z')

#func(a=1, b=2, 'x', 'y', 'z')

def func2(a, b=2, c=3, *args):
    print(a, b, c, args)

func2(1, 2, 3, 'x', 'y', 'z')
func2(1, c=5)
#func2(1, c=5, 'x', 'y')

def func3(a, b=2, *args, c=3, d):
    print(a, b, args, c, d)

func3(10, 20, 'x', 'y', 'z', c=4, d=1)
func3(10, 20, 'x', 'y', 'z', d=10)
#func3(1, 'x', 'y', 'z', b=4, d=10)
func3(1, 'x', 'y', 'z', d=10)


