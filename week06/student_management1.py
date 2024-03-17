# student_management1.py
# this function takes input to input or view student grades
# this is the first funcion in the student management suite of functions, each building upon the previous
# Author Ellen McGrory

def displayMenu(): 
    print("What would you like to do?") 
    print("\t(a) Add new student") 
    print("\t(v) View students") 
    print("\t(q) Quit") 
    choice = input("Type one letter (a/v/q):").strip() 
    
    return choice 

# tesing the built function
choice = displayMenu() 
print(f"you chose { choice }")