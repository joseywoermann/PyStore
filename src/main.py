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
    "price": 1,
    "stock": 20
}

mango = {
    "category": "fruit",
    "price": 3,
    "stock": 15
}


# Is the store open?
open = True


while open == True:

    command = input("What do you want to do?\n(buy, money, exit)\n\n>")

    clear()



    if command == "buy":
        print("Started ordering-menu...")


        print("Inventory:\n")
        for x in range(len(inventory)):
	           print("Item: " + inventory[x]) #costs XYZ


        # What product the customer wants
        selection = input("What product do you want to buy?\n>")

        clear()


        print("\n")

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

        sleep(1)
        print("\n")

        purchase_amount = input("Specify the amount of " + str(selection) + "s you want to purchase?\n>")

        if purchase_amount == "exit":
            print("Exiting store...")
            open = False

            clear()

        elif int(purchase_amount) <= stock:
            purchase = input("Do you want to purchase " + str(purchase_amount) + " " + str(selection) + "s?\n(yes, no)\n>")

            if purchase == "yes":

                if selection == "apple":
                    apple["stock"] = int(apple["stock"]) - int(purchase_amount)

                if selection == "banana":
                    banana["stock"] = int(banana["stock"]) - int(purchase_amount)

                if selection == "mango":
                    mango["stock"] = int(mango["stock"]) - int(purchase_amount)

            else:
                print("Canceled order. Thank you for visiting.")

        # TODO: if selection == xyz, charge money, reduce stock etc
        #print(apple["stock"])
        #print("You bought an apple!")
        #apple["stock"] = int(apple["stock"]) - 1
        #print(apple["stock"])




    elif command == "money":
        print("Started finace-menu...")



    elif command == "exit":
        print("Exiting store...")
        open = False
