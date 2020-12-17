from time import sleep
import os
import json

clear = lambda: os.system('cls')


clear()
print("Resetting all values to default...")
sleep(0.4)
print("Done")



appledata = {}
bananadata = {}
mangodata = {}

userdata = {}
storedata = {}


appledata["category"] = "fruit"
appledata["stock"] = 30
appledata["price"]  = 1

bananadata["category"] = "fruit"
bananadata["stock"] = 20
bananadata["price"]  = 2

mangodata["category"] = "fruit"
mangodata["stock"] = 15
mangodata["price"]  = 3


userdata["money"] = 100
storedata["money"] = 10000

with open("./data/money/customer_money.json", "w") as userfile:
    json.dump(userdata, userfile, indent=2)

with open("./data/money/store_money.json", "w") as storefile:
    json.dump(storedata, storefile, indent=2)


with open("./data/inventory/apple.json", "w") as applefile:
    appledata = json.dump(appledata, applefile, indent=2)

with open("./data/inventory/banana.json", "w") as bananafile:
    bananadata = json.dump(bananadata, bananafile, indent=2)

with open("./data/inventory/mango.json", "w") as mangofile:
    mangodata = json.dump(mangodata, mangofile, indent=2)
