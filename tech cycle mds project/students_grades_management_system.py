# Initialize the dictionary to store student names and their grades
students = {}

def add_student():
    name = input("Enter the student's name: ")
    if name in students:
        print(f"Student {name} already exists.")
        return
    
    grades = []
    while True:
        try:
            grade = float(input("Enter a grade (or type 'done' to finish): "))
            grades.append(grade)
        except ValueError:
            print("Type 'done' to finish or enter a valid number.")
            break
    
    students[name] = grades
    print(f"Student {name} added with grades: {grades}")

def view_student_details():
    name = input("Enter the student's name: ")
    if name not in students:
        print(f"No records found for student {name}.")
        return
    
    grades = students[name]
    average = sum(grades) / len(grades)
    print(f"Details for {name}:")
    print(f"Grades: {grades}")
    print(f"Average Grade: {average:.2f}")
    print(f"Pass/Fail Status: {get_pass_fail_status(average)}")

def get_pass_fail_status(average, passing_grade=60.0):
    return "Pass" if average >= passing_grade else "Fail"

def main_menu():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. View Student Details")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_student_details()
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main_menu()

