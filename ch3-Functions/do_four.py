def do_twice(f, s):
    f(s)
    f(s)

def do_four(f, s):
    do_twice(f, s)
    do_twice(f, s)


def print_twice(s):
    print(s)
    print(s)

def print_spam():
    print('spam')

do_four(print_twice, 'spam')
