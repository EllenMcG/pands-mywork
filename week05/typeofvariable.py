# type.py
# This progam prints out the type of a variable including int, list, dict, etc
# Author Ellen McGrory

# code block 
numberOfQuestions = 5 
averageAge = 23.4 
debugMode = True 
name = "joe" 
ages = [] 
months = ('Jan', 'Feb', 'Mar') 
book = {} 
stuff = [ 12 , 'Fred', False, {}] 
someone = dict(firstname = "joe") 
me = { 
    "firstName" : "Andrew", 
    "teaching" : [{ 
        "courseName" : "programming",
          "semester" : 1 
          },{ 
              "courseName" : "Data Representation", 
              "semester" : 2 
            } 
            ] 
}


# type of variables

print(type(numberOfQuestions))
print(type(averageAge))
print(type(debugMode))
print(type(name))
print(type(ages))
print(type(months))
print(type(months[1]))
print(type(book))
print(type(stuff))
print(type(stuff[2]))
print(type(someone))
print(type(someone["firstname"]))
print(type(me))
print(type(me["teaching"]))
print(type(me["teaching"][0]["semester"]))