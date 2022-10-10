# Question 1
# Given a list of filenames, we want to rename all the files with extension hpp to the extension h.
# To do this, we would like to generate a new list called newfilenames, consisting of the new filenames.
# Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for i in filenames:
	if i.endswith('.hpp'):
		hpp = '.hpp'
		h= '.h'
		i = i.replace(hpp,h)
		print(i)
		newfilenames.append(i)
	else:
		newfilenames.append(i)

print(newfilenames)

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames=[]
for filename in filenames:
	if filename.endswith(".hpp"):
		filename=filename.replace(".hpp",".h")
		newfilenames.append(filename)
	else :
		newfilenames.append(filename)

print(newfilenames)

#print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

newfilenames = [i.replace("hpp","h") for i in filenames]
print(newfilenames)

newfilenames = [filename.replace(".hpp", ".h") if filename.endswith(".hpp") else filename for filename in filenames]
print(newfilenames)

# Question 2
# Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving
# the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.

def pig_latin(text):
	say = ""
	# Separate the text into words
	newtext = []
	words = text.split()
	for word in words:
		# Create the pig latin word and add it to the list
		say = word[1:] + word[0] + "ay"
		newtext.append(say)
	# Turn the list back into a phrase
	return " ".join(newtext)

# alternatif
def pig_latin(text):
  say = ""
  words = text.split()
  for word in words:
    pig_word = word[1:] + word[0] + "ay "
    say += pig_word
  return say

print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"


# 3.
# Question 3
# The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute
# for the owner, group, and others. Each of the three values can be expressed as an octal number summing each
# permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using
# the letters r, w, and x or - when the permission is not granted.
#  For example:
#  640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string,
#  it would be: "rw-r-----"
#  755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would
#  be: "rwxr-xr-x"
#  Fill in the blanks to make the code convert a permission in octal format into a string format.

def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]

    for digit in [int(n) for n in str(octal)]:       # Iterate over each of the digits in octal [int(n) for n in str(octal)]
        for value, letter in value_letters:          # Check for each of the permissions values
            if digit >= value:
                result += letter
                digit = digit - value
            else:
                result += '-'
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------

# 5.
# Question 5
# The group_list function accepts a group name and a list of members, and returns a string with
# the format: group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c".
# Fill in the gaps in this function to do that.

def group_list(group, users):
  members = ___
  return ___

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

#def group_list(group, users):
 # members = ', '.join(users)
  #return ('{}: {}'.format(group, members))


# 6.
# Question 6
# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest,
# and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"),
# ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef.
# Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer.
# Fill in the gaps in this function to do that.

def guest_list(guests):
	for ___ in guests:
		___
		print(___.format(___))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code

#Output should match:
#Ken is 30 years old and works as Chef
#Pat is 35 years old and works as Lawyer
#Amanda is 25 years old and works as Engineer

def guest_list(guests):
	for guestinfo in guests:
		name, age, job = guestinfo
		print('{} is {} years old and works as {}'.format(name, age, job))

