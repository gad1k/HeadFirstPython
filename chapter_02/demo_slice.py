book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)

print(booklist)
print(booklist[0:3])
print("".join(booklist[0:3]))
print("".join(booklist[-6:]))

backwards = booklist[::-1]
print("".join(backwards))

every_other = booklist[::2]
print("".join(every_other))

print("".join(booklist[4:14]))
print("".join(booklist[13:3:-1]))
