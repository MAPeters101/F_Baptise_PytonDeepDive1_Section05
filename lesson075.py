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
print()

def func4(a, b=2, *args, c=10, d=20, **kwargs):
    print(a, b, args, c, d, kwargs)

func4(1, 2, 'x', 'y', 'z', c=100, d=200, x=0.1, y=0.2)
print()

#help(print)
print(1, 2, 3)
print(4, 5, 6)
print(1, 2, 3, sep='-', end=' *** ')
print(4, 5, 6, sep='-')
print('='*20)

def calc_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = min(args) if len(args) > 0 else 0
    # if len(args) == 0:
    #     lo = 0
    # else:
    #     lo = min(args)
    avg = (hi + lo) / 2
    if log_to_console:
        print("high={0}, low={1}, avg={2}".format(hi, lo, avg))
    return avg

avg = calc_hi_lo_avg(1, 2, 3, 4, 5)
print(avg)

is_debug = True
avg = calc_hi_lo_avg(1, 2, 3, 4, 5, log_to_console=is_debug)
print(avg)



