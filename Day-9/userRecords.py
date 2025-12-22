# This is the file for  user records management  with dictionary for day 9
user_records = {}
def add_user(user_id, name, email):
    user_records[user_id] = {
        "name": name,
        "email": email
    }
    print(f"User {name} added with ID {user_id}.")
def remove_user(user_id):
    if user_id in user_records:
        del user_records[user_id]
        print(f"User with ID {user_id} removed.")
    else:
        print(f"User with ID {user_id} not found.")
def view_users():
    if user_records:
        print("User Records:")
        for user_id, info in user_records.items():
            print(f"ID: {user_id}, Name: {info['name']}, Email: {info['email']}")
    else:
        print("No user records available.")
def main():
    while True:
        print("\nUser Records Management System")
        print("1. Add User")
        print("2. Remove User")
        print("3. View Users")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            add_user(user_id, name, email)
        elif choice == '2':
            user_id = input("Enter user ID to remove: ")
            remove_user(user_id)
        elif choice == '3':
            view_users()
        elif choice == '4':
            print("Exiting the User Records Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()