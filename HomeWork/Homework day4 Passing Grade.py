def all(name,midterm,project,final): #I set up function for calculation
    
    passingGrade = midterm*(0.3)+ project*(0.3)+ final*(0.4) #passing grade formula
    
    total_list = [name,midterm,project,final,passingGrade] #list where all values are summed up

    print(total_list)

    dict1 = {"Name:\n":name,
              "Midterm:\n":midterm,
              "Project:\n":project,
              "Final:\n":final,
              "passingGrade:\n":passingGrade}#glossary of all data

    passingGrade_list.append(dict1)
    
    total_grade.append(passingGrade)
    
    print_grade = [name,passingGrade]
    
    print_total.append(print_grade)
    
#-----------------------------------------------------------------------------------------------------------    

amount = 0   

passingGrade_list = []

total_grade =[]

print_total = []

while amount <= 4:     
    name = input("\nPlease enter name:")
    midterm = float(input("Enter Midterm Grade:"))
    project = float(input("Enter Project Grade:"))
    final = float(input("Enter Final Grade:"))
    amount +=1
    
    all(name,midterm,project,final)
    
    print("-----------------------------------------")
    
#-----------------------------------------------------------------------------------------------------------

inline_list = sorted(total_grade, reverse=True)

print("-----------------------------------------")

print("The initial version of the scoring:",print_total)

print("""\nRanking from the highest score to the lowest score:""",inline_list)
    
