def func(**kwargs):
    print(kwargs)

func(a=1, b=2, c=3)
print()

def func1(*args, **kwargs):
    print(args, kwargs)

#func1(1, 2, x=100, y=200, 12)
func1(1, 2, x=100, y=200)
print()

# def func2(a, b, *, **kwargs):
#     print(a, b, kwargs)

def func2(a, b, *, d, **kwargs):
    print(a, b, d, kwargs)

func2(1, 2, d=20, x=100, y=200)
func2(1, 2, x=100, y=200, d=20)
print()

def func3(a, b, **kwargs):
    print(a, b, kwargs)

func3(1, 2, x=100, y=200)
print()




