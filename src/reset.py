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


appledata["stock"] = 15
bananadata["stock"] = 20
mangodata["stock"] = 15


userdata["money"] = 100
storedata["money"] = 10000

with open("./data/money/customer_money.json", "w") as userfile:
    json.dump(userdata, userfile)

with open("./data/money/store_money.json", "w") as storefile:
    json.dump(storedata, storefile)


with open("./data/inventory/apple.json", "w") as applefile:
    appledata = json.dump(mangodata, applefile)

with open("./data/inventory/banana.json", "w") as bananafile:
    bananadata = json.dump(bananadata, bananafile)

with open("./data/inventory/mango.json", "w") as mangofile:
    mangodata = json.dump(mangodata, mangofile)
