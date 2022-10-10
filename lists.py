# The skip_elements function returns a list containing every other element from an input list, starting with the first element.
# Complete this function to do that, using the for loop to iterate through the input list.

	# Initialize variables
    new_list = []
	i = 0

	# Iterate through the list
	for every_other in elements:                                 # OR WITHOUT İ;  for element in elements[::2]:
		# Does this element belong in the resulting list?
		if i%2 == 0:
			# Add this element to the resulting list
			new_list.append(every_other)
		# Increment i
		i += 1

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

# LISTS AND TUPLES

# Let's use tuples to store information about a file: its name, its type and its size in bytes.
# Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.
def file_size(file_info):
	name, typ, size= file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

# ENUMERATE

winners = ['Ashley', 'Dylan', 'Reese']
for index, person in enumerate(winners):
	print('{} - {}'.format(index+1, person) )

# Skip_elements() function using enumerate() function

def skip_elements(elements):
	result = []
	for index, element in enumerate(elements):     # result = [element for index, element in enumerate(elements) if index%2==0]
		if index%2 == 0:
			result.append(element)
	return result

# **************************************************************

	# Say you have a list of tuples containing two strings each.
	# The first string is an email address and the second is the
	# full name of the person with that email address. You want to
	# write a function that creates a new list containing one
	# string per person including their name and the email address
	# between angled brackets. the format usually used in emails
	# like this. So what do we need to do?

def full_emails(people):  # people = tuple (first string is email,second is the full name
	result = []
	for email, name in people:
		result.append('{} <{}>'.format(name, email))
	return result

print(full_emails([('alex@example.com', 'Alex Diego'), ('eli@gmail.com', 'Eli Dagli')]))

# ********************************************************************************************************
# LIST COMPREHENSION

# The odd_numbers function returns a list of odd numbers between 1 and n, inclusively.
# Fill in the blanks in the function, using list comprehension
def odd_numbers(n):
	return [x for x in range(1, n+1) if x%2==1]





