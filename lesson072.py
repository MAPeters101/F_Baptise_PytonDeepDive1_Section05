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
print('-'*20)

def func5(a, b, *, d):
    print(a, b, d)

#func5(1, 2, 3, d=4)
func5(1, 2, d=4)

def func6(a, b=2, *args, d):
    print(a, b, args, d)

func6(1, 5, 3, 4, d='a')

def func7(a, b=20, *args, d=0, e):
    print(a, b, args, d, e)

#func7(5, 4, 3, 2, 1)
func7(5, 4, 3, 2, 1, e = 'all engines running')
print()
func7(0, 600, d='good morning', e = 'python')
func7(11, 'm/s', 24, 'mph', d='unladen', e = 'swallow')





