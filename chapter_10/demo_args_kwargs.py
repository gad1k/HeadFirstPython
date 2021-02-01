def func1(*args):
    for a in args:
        print(a, end=" ")
    if args:
        print()


def func2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep="->", end=" ")
    if kwargs:
        print()


def func3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=" ")
        print()

    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep="->", end=" ")
        print()


func1(10)
func1(10, 20, 30)
func2(a=10, b=20)
func2()
func3(1, 2, 3)
func3(a=10, b=20)
func3(3, 4, a=10, b=20)