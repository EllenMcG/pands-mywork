# student_management3.py
# this function takes input to input or view student grades
# this is the third funcion in the student management suite of functions, each building upon the previous
# this part of the program assessing if student data can be read in
# Author Ellen McGrory

students= [] 
def readModules():
     return [] 

def doAdd(students): 
    currentStudent = {} 
    currentStudent["name"]=input("enter name :") 
    currentStudent["modules"]= readModules() 
    students.append(currentStudent) 

# tesing the built function to add student name
doAdd(students) 
doAdd(students) 
print(students)