import time

def time_it(fn, *args, rep=1, **kwargs):
    # print(args, kwargs)
    for i in range(rep):
        fn(*args, **kwargs)





time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5)





