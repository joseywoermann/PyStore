from time import sleep
import os
import json

clear = lambda: os.system('cls')

# Store inventory

inventory = ['apple', 'banana', 'mango']


# Is the store open?
openstore = True

clear()
print("Starting PyStore...")
sleep(2)

while openstore is True:

    appledata = {}
    bananadata = {}
    mangodata = {}

    userdata = {}
    storedata = {}


    # Inventory
    with open("./data/inventory/apple.json") as applefile:
        appledata = json.load(applefile)

    with open("./data/inventory/banana.json") as bananafile:
        bananadata = json.load(bananafile)

    with open("./data/inventory/mango.json") as mangofile:
        mangodata = json.load(mangofile)


    # Money
    with open("./data/money/customer_money.json") as userfile:
        userdata = json.load(userfile)

    with open("./data/money/store_money.json") as storefile:
        storedata = json.load(storefile)


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

        print("Your money: $" + str(userdata["money"]) + "\n")
        print("Inventory:\n")

        for x in range(len(inventory)):
               print("Item: " + inventory[x])

        print("_____________")

        # What product the customer wants
        selection = input("\nWhat product do you want to buy?\n\n>")

        clear()
        print("Your money: $" + str(userdata["money"]) + "\n")

        print("Prices:\n")


        if selection == "apple":
            print(str("One apple: $") + str(appledata["price"]))
            print(str("In stock: ") + str(appledata["stock"]))
            stock = int(appledata["stock"])

        if selection == "banana":
            print(str("One banana: $") + str(bananadata["price"]))
            print(str("In stock: ") + str(bananadata["stock"]))
            stock = int(bananadata["stock"])

        if selection == "mango":
            print(str("One mango: $") + str(mangodata["price"]))
            print(str("In stock: ") + str(mangodata["stock"]))
            stock = int(mangodata["stock"])

        print("_____________")
        sleep(1)

        purchase_amount = input("\nSpecify the amount of " + str(selection) + "s you want to purchase?\n\n>")

        clear()
        print("Your money: $" + str(userdata["money"]) + "\n")


        if purchase_amount == "exit":
            print("Exiting store...")
            sleep(2)
            openstore = False

        elif int(purchase_amount) <= stock:
            purchase = input("Do you want to purchase " + str(purchase_amount) + " " + str(selection) + "s?\n(y, n)\n\n>")


            if purchase == "y":

                clear()
                print("Your money: $" + str(userdata["money"]) + "\n")

                if selection == "apple":
                    bill = int(purchase_amount) * int(appledata["price"])

                if selection == "banana":
                    bill = int(purchase_amount) * int(bananadata["price"])

                if selection == "mango":
                    bill = int(purchase_amount) * int(mangodata["price"])


                # Buy if enough money
                if userdata["money"] >= int(bill):

                    if selection == "apple":
                        appledata["stock"] = int(appledata["stock"]) - int(purchase_amount)

                    if selection == "banana":
                        bananadata["stock"] = int(bananadata["stock"]) - int(purchase_amount)


                    if selection == "mango":
                        mangodata["stock"] = int(mangodata["stock"]) - int(purchase_amount)

                    userdata["money"] = userdata["money"] - int(bill)
                    storedata["money"] = storedata["money"] + int(bill)

                    # Charge customer some money and add that to the sore's "bank-account"
                    with open("./data/money/customer_money.json", "w") as userfile:
                        json.dump(userdata, userfile, indent=2)

                    with open("./data/money/store_money.json", "w") as storefile:
                        json.dump(storedata, storefile, indent=2)


                    with open("./data/inventory/apple.json", "w") as applefile:
                        appledata = json.dump(mangodata, applefile, indent=2)

                    with open("./data/inventory/banana.json", "w") as bananafile:
                        bananadata = json.dump(bananadata, bananafile, indent=2)

                    with open("./data/inventory/mango.json", "w") as mangofile:
                        mangodata = json.dump(mangodata, mangofile, indent=2)

                    print("Thank you for ordering " + str(purchase_amount) + " " + str(selection) + "s!\nYou paid: $" + str(bill))

                else:
                    print("You don't have enough money to purchase " + str(purchase_amount) + " " + str(selection) + "s." + " You need $" + str(bill - userdata["money"]))
                sleep(2)
                clear()
                print("Your money: $" + str(userdata["money"]) + "\n")

            else:
                clear()
                print("Your money: $" + str(userdata["money"]) + "\n")

                print("Canceled order. Thank you for visiting.")
                sleep(2)

    elif command == "money":
        print("Started finance menu..")
        sleep(1)
        clear()
        print("You have $" + str(userdata["money"]) + ".")
        sleep(2)

    elif command == "money store":
        print("Started finance menu..")
        sleep(1)
        clear()
        print("The store has $" + str(userdata["money"]) + ".")
        sleep(2)


    elif command == "exit":
        print("Exiting store...")
        openstore = False
