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
                    for j in range(0, n - i - 1): 
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


