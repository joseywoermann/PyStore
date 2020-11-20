from time import sleep
import os
import json

clear = lambda: os.system('cls')

# Store inventory

inventory = ['apple', 'banana', 'mango']





# Import all required data from JSONs

# Items
apple = open("./data/inventory/apple.json", "r+")
banana = open("./data/inventory/banana.json", "r+")
mango = open("./data/inventory/mango.json", "r+")

# Money
customer = open("./data/money/customer_money.json", "r+")
store = open("./data/money/store_money.json", "r+")



# Read those files

# Items
details_apple = json.load(apple)
details_banana = json.load(banana)
details_mango = json.load(mango)

# Money
money_customer = json.load(customer)
money_store = json.load(store)



# Is the store open?
open = True

clear()
print("Starting PyStore...")
sleep(2)

while open == True:

    clear()

    print("Welcome to PyStore!")

    sleep(1)
    clear()

    command = input("What do you want to do?\n(buy, money, exit)\n\n>")

    clear()



    if command == "buy":
        print("Starting ordering-menu...")

        sleep(2)
        clear()

        print("Your money: $" + str(money_customer["money"]) + "\n")
        print("Inventory:\n")

        for x in range(len(inventory)):
	           print("Item: " + inventory[x]) #costs XYZ

        print("_____________")

        # What product the customer wants
        selection = input("\nWhat product do you want to buy?\n\n>")

        clear()
        print("Your money: $" + str(money_customer["money"]) + "\n")

        print("Prices:\n")


        if selection == "apple":
            print(str("1 apple: $") + str(details_apple["price"]))
            print(str("In stock: ") + str(details_apple["stock"]))
            stock = int(details_apple["stock"])

        if selection == "banana":
            print(str("1 banana: $") + str(details_banana["price"]))
            print(str("In stock: ") + str(details_banana["stock"]))
            stock = int(details_banana["stock"])

        if selection == "mango":
            print(str("1 mango: $") + str(details_mango["price"]))
            print(str("In stock: ") + str(details_mango["stock"]))
            stock = int(details_mango["stock"])

        print("_____________")
        sleep(1)

        purchase_amount = input("\nSpecify the amount of " + str(selection) + "s you want to purchase?\n\n>")

        clear()
        print("Your money: $" + str(money_customer["money"]) + "\n")

        if purchase_amount == "exit":
            print("Exiting store...")
            sleep(2)
            open = False

        elif int(purchase_amount) <= stock:
            purchase = input("Do you want to purchase " + str(purchase_amount) + " " + str(selection) + "s?\n(y, n)\n\n>")


            if purchase == "y":

                clear()
                print("Your money: $" + str(money_customer["money"]) + "\n")

                if selection == "apple":
                    bill = int(purchase_amount) * int(details_apple["price"])

                if selection == "banana":
                    bill = int(purchase_amount) * int(details_banana["price"])

                if selection == "mango":
                    bill = int(purchase_amount) * int(details_mango["price"])


                # Buy if enough money
                if money_customer["money"] >= int(bill):

                    if selection == "apple":
                        apple["stock"] = int(apple["stock"]) - int(purchase_amount)

                    if selection == "banana":
                        banana["stock"] = int(banana["stock"]) - int(purchase_amount)


                    if selection == "mango":
                        mango["stock"] = int(mango["stock"]) - int(purchase_amount)


                    # Charge customer some money and add that to the sore's "bank-account"
                    money["customer"] = money["customer"] - int(bill)
                    money["store"] = money["store"] + int(bill)

                    print("Thank you for ordering " + str(purchase_amount) + " " + str(selection) + "s!\nYou paid: $" + str(bill))

                else:
                    print("You don't have enough money to purchase " + str(purchase_amount) + " " + str(selection) + "s." + " You need $" + str(bill - money_customer["money"]))
                sleep(2)
                clear()
                print("Your money: $" + str(money_customer["money"]) + "\n")

            else:
                clear()
                print("Your money: $" + str(money_customer["money"]) + "\n")

                print("Canceled order. Thank you for visiting.")
                sleep(2)



    elif command == "money":
        print("Started finance menu..")
        sleep(1)
        clear()
        print("You have $" + str(money_customer["money"]) + ".")
        sleep(2)

    elif command == "money store":
        print("Started finance menu..")
        sleep(1)
        clear()
        print("The store has $" + str(money_customer["money"]) + ".")
        sleep(2)


    elif command == "exit":
        print("Exiting store...")
        open = False
