#school result system

student={}

for i in range(4):
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    student[name] = marks

print("student results:", student)


marks_list = list(student.values())

def sum_of_marks(marks_list,n):
    if n <= 0:
        return 0        
    return marks_list[n-1] + sum_of_marks(marks_list,n-1)

total_marks = sum_of_marks(marks_list, len(marks_list))
print("Total marks of all students: ", total_marks)


# grade of each student
def grade(marks):

    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"          
    elif marks >= 60:
        return "D"
    else:
        return "F"  

for name, marks in student.items():
    print(f"{name} has grade: {grade(marks)}")

# average marks of students
num_students= len(student)

def average_marks(total_marks, num_students):
    return total_marks / num_students

print("Average marks of students: ", average_marks(total_marks, num_students))  


# highest marks scored by a student

highest_marks = max(student.values())
print("Highest marks scored by a student: ", highest_marks) 

highest_scorer = max(student, key=student.get)
print(f"Highest Scorer: {highest_scorer} - {student[highest_scorer]}")


