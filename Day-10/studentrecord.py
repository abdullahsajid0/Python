# Student Record Management System with dictionary and the list for day 10
# Each student has a name and a list of grades

student_records = {}
def add_student(student_id, name, grades):
    student_records[student_id] = {
        "name": name,
        "grades": grades
    }
    print(f"Student {name} added with ID {student_id}.")
def remove_student(student_id):
    if student_id in student_records:
        del student_records[student_id]
        print(f"Student with ID {student_id} removed.")
    else:
        print(f"Student with ID {student_id} not found.")
def view_students():
    if student_records:
        print("Student Records:")
        for student_id, info in student_records.items():
            grades_str = ', '.join(map(str, info['grades']))
            print(f"ID: {student_id}, Name: {info['name']}, Grades: [{grades_str}]")
    else:
        print("No student records available.")
def main():
    while True:
        print("\nStudent Record Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. View Students")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            grades_input = input("Enter student grades separated by commas: ")
            grades = [(grade.strip()) for grade in grades_input.split(',')]
            add_student(student_id, name, grades)
        elif choice == '2':
            student_id = input("Enter student ID to remove: ")
            remove_student(student_id)
        elif choice == '3':
            view_students()
        elif choice == '4':
            print("Exiting the Student Record Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
