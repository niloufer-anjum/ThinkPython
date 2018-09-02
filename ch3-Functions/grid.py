from __future__ import print_function

def plus(end):
    print('+', end=end)

def minus():
    print('- ', end=' ')

def space():
    print('  ', end=' ')

def pipe(end):
    print('|', end=end)

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def do_twice2(f, g, h):
    f()
    g(h)
    f()
    g(h)

def beam():
    return(plus('  '), do_four(minus))

def beam2():
    do_twice(beam)
    plus('\n')

def beam4():
    do_four(beam)
    plus('\n')

def post():
    return(pipe('  '), do_four(space))

def post2():
    do_twice(post)
    pipe('\n')

def post4():
    do_four(post)
    pipe('\n')

def grid2():
    beam2()
    do_four(post2)
    beam2()

def grid4():
    do_twice2(beam2, do_four, post2)
    beam2()

def grid8():
    do_twice2(beam4, do_four, post4)
    do_twice2(beam4, do_four, post4)
    beam4()

grid8()
