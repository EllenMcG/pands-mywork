# studen_management2.py
# this function takes input to input or view student grades
# this is the second funcion in the student management suite of functions, each building upon the previous
# this part of the program stops when user enteres q for quit
# Author Ellen McGrory

def displayMenu(): 
    print("What would you like to do?") 
    print("\t(a) Add new student") 
    print("\t(v) View students") 
    print("\t(q) Quit") 
    choice = input("Type one letter (a/v/q):").strip() 
    return choice 

def doAdd(): 
    print("in adding") 
    
def doView(): 
    print("in viewing")

# tesing the built function
choice = displayMenu() 
while(choice != 'q'): 
    if choice == 'a': 
        doAdd() 
    elif choice == 'v': 
        doView() 
    elif choice !='q': 
        print("\n\nplease select either a,v or q")
    choice=displayMenu()