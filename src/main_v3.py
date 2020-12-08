
"""
TODO:
-files can't be updated while the script is running, JSONs must be re-loaded when needed
-overwrite values in JSONs
"""

from time import sleep
import os
import json

clear = lambda: os.system('cls')

# Store inventory

inventory = ['apple', 'banana', 'mango']





# Import all required data from JSONs

# Items
apple_fileR = open("./data/inventory/apple.json", "r")
details_appleR = json.load(apple_fileR)
#apple_fileR.close()

banana_fileR = open("./data/inventory/banana.json", "r")
details_bananaR = json.load(banana_fileR)
#banana_fileR.close()

mango_fileR = open("./data/inventory/mango.json", "r")
details_mangoR = json.load(mango_fileR)
#mango_fileR.close()

# Money
customer_fileR = open("./data/money/customer_money.json", "r")
money_customerR = json.load(customer_fileR)
#customer_fileR.close()

store_fileR = open("./data/money/store_money.json", "r")
money_storeR = json.load(store_fileR)
#store_fileR.close()



# Items
apple_fileW = open("./data/inventory/apple.json", "w")
details_appleW = json.load(apple_fileW)
#apple_fileW.close()

banana_fileW = open("./data/inventory/banana.json", "w")
details_bananaW = json.load(banana_fileW)
#banana_fileW.close()

mango_fileW = open("./data/inventory/mango.json", "w")
details_mangoW = json.load(mango_fileW)
#mango_fileW.close()

# Money
customer_fileW = open("./data/money/customer_money.json", "w")
money_customerW = json.load(customer_fileW)
#customer_fileW.close()

store_fileW = open("./data/money/store_money.json", "w")
money_storeW = json.load(store_fileW)
#store_fileW.close()


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

        print("Your money: $" + str(money_customerR["money"]) + "\n")
        print("Inventory:\n")

        for x in range(len(inventory)):
	           print("Item: " + inventory[x]) #costs XYZ

        print("_____________")

        # What product the customer wants
        selection = input("\nWhat product do you want to buy?\n\n>")

        clear()
        print("Your money: $" + str(money_customerR["money"]) + "\n")

        print("Prices:\n")


        if selection == "apple":
            print(str("1 apple: $") + str(details_appleR["price"]))
            print(str("In stock: ") + str(details_appleR["stock"]))
            stock = int(details_appleR["stock"])

        if selection == "banana":
            print(str("1 banana: $") + str(details_bananaR["price"]))
            print(str("In stock: ") + str(details_bananaR["stock"]))
            stock = int(details_bananaR["stock"])

        if selection == "mango":
            print(str("1 mango: $") + str(details_mangoR["price"]))
            print(str("In stock: ") + str(details_mangoR["stock"]))
            stock = int(details_mangoR["stock"])

        print("_____________")
        sleep(1)

        purchase_amount = input("\nSpecify the amount of " + str(selection) + "s you want to purchase?\n\n>")

        clear()
        print("Your money: $" + str(money_customerR["money"]) + "\n")

        if purchase_amount == "exit":
            print("Exiting store...")
            sleep(2)
            open = False

        elif int(purchase_amount) <= stock:
            purchase = input("Do you want to purchase " + str(purchase_amount) + " " + str(selection) + "s?\n(y, n)\n\n>")


            if purchase == "y":

                clear()
                print("Your money: $" + str(Money_customerR["money"]) + "\n")

                if selection == "apple":
                    bill = int(purchase_amount) * int(details_appleR["price"])

                if selection == "banana":
                    bill = int(purchase_amount) * int(details_bananaR["price"])

                if selection == "mango":
                    bill = int(purchase_amount) * int(details_mangoR["price"])


                # Buy if enough money
                if money_customerR["money"] >= int(bill):

                    if selection == "apple":
                        details_appleR["stock"] = int(details_appleR["stock"]) - int(purchase_amount)

                    if selection == "banana":
                        details_bananaR["stock"] = int(details_bananaR["stock"]) - int(purchase_amount)


                    if selection == "mango":
                        details_mangoR["stock"] = int(details_mangoR["stock"]) - int(purchase_amount)





                    # Charge customer some money and add that to the sore's "bank-account"


                    """
                    money_customerR["money"] = 123

                    mango_fileR = open("mango.json", "w")
                    json.dump(money_customerR, mango_fileR, indent = 2, sort_keys=True)
                    mango_fileR.close()
                    """
                    money_customerR["money"] = money_customerR["money"] - int(bill)
                    money_storeR["money"] = money_storeR["money"] + int(bill)

                    json.dump(money_customerR, customer_fileR, indent = 2, sort_keys=True)
                    json.dump(money_storeR, store_fileR, indent = 2, sort_keys=True)



                    print("Thank you for ordering " + str(purchase_amount) + " " + str(selection) + "s!\nYou paid: $" + str(bill))




                else:
                    print("You don't have enough money to purchase " + str(purchase_amount) + " " + str(selection) + "s." + " You need $" + str(bill - money_customerR["money"]))
                sleep(2)
                clear()
                print("Your money: $" + str(money_customerR["money"]) + "\n")

            else:
                clear()
                print("Your money: $" + str(money_customerR["money"]) + "\n")

                print("Canceled order. Thank you for visiting.")
                sleep(2)



    elif command == "money":
        print("Started finance menu..")
        sleep(1)
        clear()
        print("You have $" + str(money_customerR["money"]) + ".")
        sleep(2)

    elif command == "money store":
        print("Started finance menu..")
        sleep(1)
        clear()
        print("The store has $" + str(money_customerR["money"]) + ".")
        sleep(2)


    elif command == "exit":
        print("Exiting store...")
        open = False
