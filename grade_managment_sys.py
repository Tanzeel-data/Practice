student = {}

def add_grade():
  name = input("enter the student name")
  grade = input("enter the grade")

  student[name.lower()]=grade.lower()
  print(f"{name} has been added with grade {grade}")

def show_all_grades():
    if student == {}:
        print("No grades have been added yet.")
    else:
        print("---Grades---")
        for name, grade in student.items():
            print(f"{name}: {grade}")

def show_specific_grade():
  st_name = input("enter the student name").lower()
  if st_name in student:
    print(f"{st_name}: {student[st_name]}")

  else:
    print(f"{st_name} not found")

def update_grade():
  st_name = input("enter the student name").lower()
  if st_name in student:
    new_grade = input("enter the new grade").lower()
    student[st_name] = new_grade
    print(f"{st_name}'s grade has been updated to {new_grade}")
  else:
    print(f"{st_name} not found")

def delete_grade():
  st_name = input("enter the student name").lower()
  if st_name in student:
    del student[st_name]
    print(f"{st_name} has been deleted")
  else:
    print(f"{st_name} not found")

def menu():
    while True:
        print("\n1. Add grade")
        print("2. Show all grades")
        print("3. Show specific grade")
        print("4. Update grade")
        print("5. Delete grade")
        print("6. Exit")

        try:
            choose = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if choose == 1:
            add_grade()
        elif choose == 2:
            show_all_grades()
        elif choose == 3:
            show_specific_grade()
        elif choose == 4:
            update_grade()
        elif choose == 5:
            delete_grade()
        elif choose == 6:
            print("Exiting Program...\n")
            print("Thank you for using Grade Management System!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    print("Welcome to Grade Management System!")
    menu()