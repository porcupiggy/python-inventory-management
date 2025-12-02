# write a program to manage a list of inventory items at a pawn shop
# the program will be used by the shopkeeper to enter items into the inventory and remove them if necessary
# each item will have a name and a price. items are identified uniquely by name.


# when the program starts, it should inform the user how many items are in the inventory
# and then print the following MAIN menu:

# 1. add an item to the inventory
# 2. remove an item from the inventory
# 3. print the inventory
# 4. exit the program

# if the user chooses to add an item to the inventory,
    # the program should ask for the item name and price and add it to the program
        # (ensure to check if the item already exists in the inventory, and also ensure that the price is a valid number, if that is not the case
        # print an error message and return to the MAIN menu)
    # then, print a message saying that the item has been added to the inventory and return to the MAIN menu

# otherwise if the user chooses to remove an item from the inventory,
    # the program should ask for the item name and remove it from the inventory
    # (ensure to check if the item exists in the inventory)
    # then, print a message saying that the item has been removed from the inventory and return to the MAIN menu

# otherwise if the user chooses to print the inventory,
    # the program should print the inventory from top to bottom in alphabetically sorted order
    # then go back to the MAIN menu

# otherwise if the user chooses to exit the program,
    #  exit the program

# otherwise if the user chooses an invalid option,
    # the program should print an error message and return to the MAIN menu


# example output:

# Welcome to the Pawn Shop Inventory Management System!
# There are currently 0 items in the inventory.
# ========================================
# please choose an option:
# 1. add an item to the inventory
# 2. remove an item from the inventory
# 3. print the inventory
# 4. exit the program
# ========================================
# 1
# please enter the item name: gold ring
# please enter the item price: 100
# item added to inventory!
# ========================================
# please choose an option:
# 1. add an item to the inventory
# 2. remove an item from the inventory
# 3. print the inventory
# 4. exit the program
# ========================================
# 1
# please enter the item name: gold ring
# item already exists in inventory!
# ========================================
# please choose an option:
# 1. add an item to the inventory
# 2. remove an item from the inventory
# 3. print the inventory
# 4. exit the program
# ========================================
# 3
# gold ring: $100
# ========================================
# please choose an option:
# 1. add an item to the inventory
# 2. remove an item from the inventory
# 3. print the inventory
# 4. exit the program
# ========================================
# 2
# please enter the item name: cabbage
# item does not exist in inventory!
# ========================================
# please choose an option:
# 1. add an item to the inventory
# 2. remove an item from the inventory
# 3. print the inventory
# 4. exit the program
# ========================================
# 1
# please enter the item name: cabbage
# please enter the item price: 1
# item added to inventory!
# ========================================
# please choose an option:
# 1. add an item to the inventory
# 2. remove an item from the inventory
# 3. print the inventory
# 4. exit the program
# ========================================
# 3
# cabbage: $1
# gold ring: $100
# ========================================
# please choose an option:
# 1. add an item to the inventory
# 2. remove an item from the inventory
# 3. print the inventory
# 4. exit the program
# ========================================
# 4
# goodbye!

def pawn_shop_inventory():
    inventory = [
        {
            "name": "pearl necklace",
            "price": 400,
        },
        {
            "name": "diamond ring",
            "price": 1200
        }
    ]
    print("welcome to my pawn shop")
    print(f"this is how many items are currently in inventory {len(inventory)}")
    while True:
        print("please select an option")
        print("1. add an item to the inventory")
        print("2. remove an item from inventory")
        print("3. print the inventory")
        print("4. exit the program")
        option = input()

        if option == "1":
            print("please enter the name of the item")
            item_name = input()
            print("please enter the price of the item")
            item_price = int(input())
            for item in inventory:
                if item["name"] == item_name:
                    print("this item is already in the inventory!")
                    break
            else:
                inventory.append({"name":item_name, "price":item_price})
                print("item has been added to inventory!")

        elif option == "2":
            print("please enter the name of the item")
            item_name = input()
            for i in range(len(inventory)):
                if inventory[i]['name'] == item_name:
                    inventory.pop(i)
                    print("the item has been removed from the inventory")
                    break
                print("item has been removed from the inventory")
            else:
                print("this item does not exist in the inventory")
        
        elif option == "3":
            if len(inventory) == 0:
                print("inventory is empty")
            else:
                n = len(inventory)
                for i in range(n):
                    for j in range(0, n - i - 1): # i used the bubble sort that jamie taught me, it was the only thing i could rememeber during the test LOL
                        if inventory[j]['name'] > inventory[j + 1]['name']:
                            inventory[j], inventory[j + 1] = inventory[j + 1], inventory[j]
                for item in inventory:
                    print(item["name"], ": $", item["price"])
    
        elif option == "4":
            print("goodbye!")
            break
        else:
            print("invalid option! please try again")


pawn_shop_inventory()
