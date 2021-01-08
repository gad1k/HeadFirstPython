def double(arg):
    print("Before:", arg)
    arg = arg * 2
    print("After", arg)


def change(arg):
    print("Before:", arg)
    arg.append("More data")
    print("After", arg)


saying = "Hello"
double(saying)
print(saying)

numbers = [42, 256, 16]
change(numbers)
print(numbers)
