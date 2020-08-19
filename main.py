from human import People
from making_csv import make_csv

file_name = "foodie.csv"

panpee = People()
panpee.say_hello()

while True:
    name = input()
    if len(name)>=1:break

panpee.asking(name)

while True:
    food = input().capitalize()
    if len(food)>=1:break

making_csv = make_csv(file_name)
making_csv.load_data()
making_csv.increase(food)
panpee.thanks(name)
