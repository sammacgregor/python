
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

