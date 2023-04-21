stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    total_items = 0
    print("Inventory:")

    for item, count in inventory.items():
        print(count, item)
        total_items += count
    
    print(f"total number of items: {total_items}")
    


if __name__ == "__main__":
    displayInventory(stuff)
