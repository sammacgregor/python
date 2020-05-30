
# hello world example
greeting = 'hello world'
print(greeting)


# if statements
if greeting == 'hello world':
    print('expected greeting')


# character input
#x = int(input("Please enter an integer: "))
#print('You have entered: ' + str(x))

# casting
x = 3
y = '0'
#print('Casted int to str is' + str(x) + 'casted str to int is ' + int(y))

# arrays
array = ['a','b','c','d','e']
print('index 0 is ' + array[0] + 'for an array of alphabet')

# for loop
array = ['a','b','c','d','e']
test = ''
for item in array:
    test += item
print(test)


# while loop
value = 1
while value != 5:
    print ('Value isnt five yet, is still: ' + str(value))
    value += 1
print('value is now ' + str(value))

# substring search
text = 'hello world'
searchString = 'r'
index = 0
textLength = len(text)
for i in text:
    if(i == searchString):
        print('found the letter ' + str(i))

# class

class ProcessInstance:
    ProcessInstanceID = 1
    ProcessDefinitionID =  1

processInstance = ProcessInstance()
print(processInstance.ProcessInstanceID)

# class with initialisation

class ProcessDefinition:
    def __init__(self, ProcessDefinitionID, ProcessDefinitionDescription):
        self.ProcessDefinitionID = ProcessDefinitionID
        self.ProcessDefinitionDescription = ProcessDefinitionDescription

p1 = ProcessDefinition(1,'Rollover Out')

print(p1.ProcessDefinitionDescription)

# class with methods



class LookupMilestone:
    def __init__(self, MilestoneID, MilestoneDescription):
        self.MilestoneID = MilestoneID
        self.MilestoneDescription = MilestoneDescription

    def getMilestone(self):
        print(self.MilestoneDescription)
    
l1 = LookupMilestone(1,'Initiated')

l1.getMilestone()


# dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)

for x, y in thisdict.items():
  print(x, y)

print(len(thisdict))

thisdict["color"] = "red"
print(thisdict)

thisdict.pop("model")
print(thisdict)

# modules

import module

module.greeting("Sam")

from module import person1

print (person1["age"])

# built in modules

import platform

x = platform.system()
print(x)

y = dir(platform)
print(y)


# dates

import datetime
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.strftime("%A")) # Day name, see https://www.w3schools.com/python/python_datetime.asp

newDate = datetime.datetime(2020,5,17)


# json

import json

newJson =  '{ "name":"John", "age":27, "city":"New York"}'

blob = json.loads(newJson) # parse x

    
print(blob["age"]) # the result is a Python dictionary:



x = { # a Python object (dict):
  "name": "John",
  "age": 30,
  "city": "New York"
}


y = json.dumps(x) # convert into JSON:


print(y) # the result is a JSON string:

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
print(json.dumps(x, indent=4))

