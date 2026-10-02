poster = int(input("Enter the number of posters: "))
customer = str(input("Are you a student? (yes/no): "))
money = int(input("Enter the money you have: "))
total = 0
price = 0
if customer == "yes":
    if poster >= 6:
        price = 7
    else:
        price = 9
else:
    if poster >= 6:
        price = 9
    else:
        price = 11
total = poster * price
print(f"Price per poster: {price}")
print(f"Total cost: {total}")
if money > total:
    left_money = money - total
    print(f"Money left: {left_money}")
elif money == total:
    print("Exactly enough money")
elif money < total:
    needed_money = total - money
    print(f"More money needed: {needed_money}")