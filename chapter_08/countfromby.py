class CountFromBy:
    def __init__(self, v: int = 0, i: int = 1) -> None:
        self.val = v
        self.incr = i

    def __repr__(self) -> str:
        return str(self.val)

    def increase(self) -> None:
        self.val += self.incr


print("Object A:")
a = CountFromBy(100, 10)
print(a.val, a.incr)
a.increase()
print(a.val, a.incr)

print("Object B:")
b = CountFromBy()
print(b.val, b.incr)
b.increase()
print(b.val, b.incr)

print("Object C:")
c = CountFromBy()
print(c)
print(type(c))
print(id(c))
print(hex(id(c)))
