import os
import csv

os.chdir("d:\\repository\\python\\HeadFirstPython\\chapter_12")

with open("buzzers.csv") as raw_data:
    print(raw_data.read())

print()

with open("buzzers.csv") as data:
    for line in csv.reader(data):
        print(line)

print()

with open("buzzers.csv") as data:
    for line in csv.DictReader(data):
        print(line)
