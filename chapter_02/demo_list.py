found = []
print(len(found))

found.append("a")
print(len(found))
print(found)

found.append("e")
found.append("i")
found.append("o")
print(len(found))
print(found)

if "u" not in found:
    found.append("u")

print(found)

nums = [1, 2, 3, 4]
print(nums)

nums.remove(3)
print(nums)

nums.pop()
print(nums)

nums.pop(0)
print(nums)

nums.extend([3, 4])
print(nums)

nums.insert(0, 1)
print(nums)

nums.insert(2, "two-and-a-half")
print(nums)
