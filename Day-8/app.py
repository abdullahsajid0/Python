# this is the program for the inventory list
inventory = []
def add_item(item):
    inventory.append(item)
    print(f"{item} has been added to the inventory.")
def remove_item(item):
    if item in inventory:
        inventory.remove(item)
        print(f"{item} has been removed from the inventory.")
    else:
        print(f"{item} not found in the inventory.")
def view_inventory():
    if inventory:
        print("Current Inventory:")
        for item in inventory:
            print(f"- {item}")
    else:
        print("The inventory is empty.")
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            print("Exiting the Inventory Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
print("Inventory management program has ended.")
print("Thank you for using the Inventory Management System.")
print(inventory)