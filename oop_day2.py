class Student:

    # Constructor
    def __init__(self, name, roll_no, department):
        self.name = name
        self.roll_no = roll_no
        self.department = department

    # Method
    def show_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Department:", self.department)


# Creating objects
student1 = Student("Ali", 101, "Computer Science")
student2 = Student("Sara", 102, "Software Engineering")

# Calling method
student1.show_details()
print()

student2.show_details()