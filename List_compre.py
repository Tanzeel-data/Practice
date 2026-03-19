if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append( [name,score])
        
    grades = [record[1] for record in records]
    
    sorted_grades = sorted(set(grades))
    
    second_lowest = sorted_grades[1]
    
    names=[] 
    
    for second in records:
        if second[1] == second_lowest:  
            names.append(second[0])
            
    names.sort() 
    
    names.sort()
    for n in names:
        print(n)

    