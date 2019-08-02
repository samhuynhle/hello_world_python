# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello", name, "!")	# with a comma
print("Hello " + name + "!")	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", name, "!")	# with a comma
print("Hello " + str(name) + "!")	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string

name = "i am sam"
new_name = name.upper()
print(new_name)
# this made all the characters in the string uppercase

name = new_name.lower()
print(name)
# this made reassigned name the lowercase values of new_name.

splitted = name.split(" ")
print(splitted)
# returned a list (similar to a JavaScript array) with the values
# of the string split at the spaces " "

count = name.count("a")
print(count)
# counted the stubstring "a" in the string of name

find = name.find("m")
print(find)
#find the position of the first "m" character in the string of name

seperator = ', '
print(seperator.join(splitted))
#joined the list, splitted, into a concatenated string where
# the values from splitted are joined by the value 
# stored in split



