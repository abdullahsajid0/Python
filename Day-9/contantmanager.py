# this is the contant manager using dictionary


contacts = {}
def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added with phone number {phone}.")   
def remove_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} removed.")
    else:
        print(f"Contact {name} not found.")
def view_contacts():
    if contacts:
        print("Contact List:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts available.")
def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. View Contacts")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            name = input("Enter contact name to remove: ")
            remove_contact(name)
        elif choice == '3':
            view_contacts()
        elif choice == '4':
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()