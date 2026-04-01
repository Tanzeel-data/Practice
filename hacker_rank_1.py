if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    query_name = input()
    
    # Get the marks list
    marks = student_marks[query_name]
    
    # Calculate average
    average = sum(marks) / len(marks)
    
    # Print with 2 decimal places
    print(f"{average:.2f}")