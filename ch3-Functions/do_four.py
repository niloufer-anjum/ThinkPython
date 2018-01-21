def do_twice(f, v):
    f(v)
    f(v)


def print_twice(s):
    print(s)
    print(s)


def do_four(func, val):
    do_twice(func, val)
    do_twice(func, val)


def print_spam():
    print('spam')


do_four(print_twice, 'spam')
