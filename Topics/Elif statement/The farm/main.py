chicken_price = 23

goat_price = 678

pig_price = 1296

cow_price = 3848

sheep_price = 6769

user_money = int(input())

if user_money >= sheep_price:
    print(f"{user_money // sheep_price} sheep")

elif user_money >= cow_price:
    if user_money >= 2 * cow_price:
        print(f"{user_money // cow_price} cows")
    else:
        print(f"{user_money // cow_price} cow")

elif user_money >= pig_price:
    if user_money >= 2 * pig_price:
        print(f"{user_money // pig_price} pigs")
    else:
        print(f"{user_money // pig_price} pig")

elif user_money >= goat_price:
    if user_money >= 2 * goat_price:
        print(f"{user_money // goat_price} goats")
    else:
        print(f"{user_money // goat_price} goat")

elif user_money >= chicken_price:
    if user_money >= 2 * chicken_price:
        print(f"{user_money // chicken_price} chickens")
    else:
        print(f"{user_money // chicken_price} chicken")

else:
    print("None")
