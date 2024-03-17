# student_management4.py
# this function takes input to input or view student grades
# this is the fifth funcion in the student management suite of functions, each building upon the previous
# this is the final function in the group and conbineds aspects of student_management1-4.py and brings them in together 
# Author Ellen McGrory

def displayMenu(): 
    print("What would you like to do?") 
    print("\t(a) Add new student") 
    print("\t(v) View students") 
    print("\t(q) Quit") 
    choice = input("Type one letter (a/v/q):").strip() 
    return choice 

def doAdd(students): 
    currentStudent = {} 
    currentStudent["name"]=input("Enter name :") 
    currentStudent["modules"]= readModules() 
    students.append(currentStudent) 
    
def readModules(): 
    modules = [] 
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip() 
    while moduleName != "": 
        module = {} 
        module["name"]= moduleName 
        module["grade"]=int(input("\t\tEnter grade:")) 
        modules.append(module) 
        moduleName = input("\tEnter next module name (blank to quit) :").strip() 
    return modules 

def doView(students): 
    for currentStudent in students: 
        print(currentStudent["name"]) 
        displayModules(currentStudent["modules"]);

def displayModules(modules): 
    print ("\tName \tGrade") 
    for module in modules: 
        print(f"\t{ module['name']} \t{ module['grade']}")

students = [] 
choice = displayMenu() 
while(choice != 'q'): 
    if choice == 'a': 
        doAdd(students) 
    elif choice == 'v': 
        doView(students) 
    elif choice !='q': 
        print("\n\nplease select either a,v or q") 
    choice=displayMenu()