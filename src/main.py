from time import sleep
import os


clear = lambda: os.system('cls')

# Store inventory

inventory = ['apple', 'banana', 'mango']


apple = {
    "category": "fruit",
    "price": 2,
    "stock": 10
}

banana = {
    "category": "fruit",
    "price": 3,
    "stock": 20
}

mango = {
    "category": "fruit",
    "price": 5,
    "stock": 15
}


# Finances

money = {
    "bank": 1000000, # 1mil
    "store": 1000, #1K
    "customer": 100
}


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

        print("Your money: $" + str(money["customer"]) + "\n")
        print("Inventory:\n")

        for x in range(len(inventory)):
	           print("Item: " + inventory[x]) #costs XYZ

        print("_____________")

        # What product the customer wants
        selection = input("\nWhat product do you want to buy?\n\n>")

        clear()
        print("Your money: $" + str(money["customer"]) + "\n")

        print("Prices:\n")


        if selection == "apple":
            print(str("1 apple: $") + str(apple["price"]))
            print(str("In stock: ") + str(apple["stock"]))
            stock = int(apple["stock"])

        if selection == "banana":
            print(str("1 banana: $") + str(banana["price"]))
            print(str("In stock: ") + str(banana["stock"]))
            stock = int(banana["stock"])

        if selection == "mango":
            print(str("1 mango: $") + str(mango["price"]))
            print(str("In stock: ") + str(mango["stock"]))
            stock = int(mango["stock"])

        print("_____________")
        sleep(1)

        purchase_amount = input("\nSpecify the amount of " + str(selection) + "s you want to purchase?\n\n>")

        clear()
        print("Your money: $" + str(money["customer"]) + "\n")

        if purchase_amount == "exit":
            print("Exiting store...")
            sleep(2)
            open = False

        elif int(purchase_amount) <= stock:
            purchase = input("Do you want to purchase " + str(purchase_amount) + " " + str(selection) + "s?\n(y, n)\n\n>")


            if purchase == "y":

                clear()
                print("Your money: $" + str(money["customer"]) + "\n")

                if selection == "apple":
                    bill = int(purchase_amount) * int(apple["price"])

                if selection == "banana":
                    bill = int(purchase_amount) * int(banana["price"])

                if selection == "mango":
                    bill = int(purchase_amount) * int(mango["price"])


                # Buy if enough money
                if money["customer"] >= int(bill):

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
                    print("You don't have enough money to purchase " + str(purchase_amount) + " " + str(selection) + "s." + " You need $" + str(bill - money["customer"]))
                sleep(2)
                clear()
                print("Your money: $" + str(money["customer"]) + "\n")

            else:
                clear()
                print("Your money: $" + str(money["customer"]) + "\n")

                print("Canceled order. Thank you for visiting.")
                sleep(2)



        #print(apple["stock"])
        #print("You bought an apple!")
        #apple["stock"] = int(apple["stock"]) - 1
        #print(apple["stock"])


    elif command == "money":
        print("Started finance menu..")
        sleep(1)
        clear()
        print("You have $" + str(money["customer"]) + ".")
        sleep(2)

    elif command == "money store":
        print("Started finance menu..")
        sleep(1)
        clear()
        print("The store has $" + str(money["store"]) + ".")
        sleep(2)


    elif command == "exit":
        print("Exiting store...")
        open = False
