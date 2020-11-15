from time import sleep





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

    if command == "buy":
        print("Started ordering-menu...")

        print("Inventory:\n")
        for x in range(len(inventory)):
	           print("Item: " + inventory[x]"""costs xyz$""")

        #print(apple["stock"])
        #print("You bought an apple!")
        #apple["stock"] = int(apple["stock"]) - 1
        #print(apple["stock"])
        selection = input("What product do you want to buy?\n")

        # TODO: if selection == xyz, charge money, reduce stock etc

    elif command == "money":
        print("Started finace-menu...")

    elif command == "exit":
        print("Exiting store...")
        open = False
