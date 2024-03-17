# grades.py
# This program stores the student name and list of courses and 
# respective grades
# Author Ellen McGrory


student = { 
    "name":"Mary", 
    "modules": [ 
        { 
            "course_name":"Programming", 
            "grade": 45 
        }, 
        { 
            "course_name":"History", 
            "grade":99 
        } 
    ] 
} 
print ("Student: {}".format(student["name"])) 
for module in student["modules"]: 
    print("\t {} \t: {}".format(module["course_name"], module["grade"]))