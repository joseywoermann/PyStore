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

    command = input("What do you want to buy?\n")
    
    if command == "apple":
        print(apple["stock"])
        print("You bought an apple!")
        apple["stock"] = int(apple["stock"]) - 1
        print(apple["stock"])
