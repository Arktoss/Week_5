import os
import math
os.system("cls")

pennies = int(input("How much pennies do you have? "))
while pennies >= 5:
    if pennies >= 100:
        print(f"Dollars = {math.floor(pennies / 100)}")
        pennies -= 100 * math.floor(pennies/100)
    elif pennies >= 25:
        print(f"Quarters = {math.floor(pennies / 25)}")
        pennies -= 25 * math.floor(pennies/25)
    elif pennies >= 10:
        print(f"Dime's = {math.floor(pennies / 10)}")
        pennies -= 10 * math.floor(pennies/10)
    elif pennies >= 5:
        print(f"Nickel's = {math.floor(pennies / 5)}")
        pennies -= 5 * math.floor(pennies/5)
print(f"pennies = {pennies}")