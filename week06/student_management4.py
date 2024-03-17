# student_management4.py
# this function takes input to input or view student grades
# this is the fourth funcion in the student management suite of functions, each building upon the previous
# this part of the program assessing if module data can be read in
# Author Ellen McGrory

def readModules(): 
    modules = [] 
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip() 

    while moduleName != "": 
        module = {} 
        module["name"]= moduleName  
        module["grade"]=int(input(f"\t\tEnter grade:")) 
        modules.append(module) 
        moduleName = input("\tEnter next module name (blank to quit) :").strip() 

    return modules