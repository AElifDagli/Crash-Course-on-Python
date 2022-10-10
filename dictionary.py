def guest_list(guests):
	for guest in guests:
		name, age, job = guest
		print('{} is {} years old and works as {}'.format(name, age, job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code

#Output should match:
#Ken is 30 years old and works as Chef
#Pat is 35 years old and works as Lawyer
#Amanda is 25 years old and works as Engineer


# 1.
# Question 1
# The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values.
# Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

def email_list(domains):
	emails = []
	for donames, users in domains.items():
		for user in users:
			emails.append('{}@{}'.format(user, donames))
	return emails

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


# 2.
# Question 2
# The groups_per_user function receives a dictionary, which contains group names with the list of users.
# Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a
# list of their groups as values.

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group_names, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			if user not in user_groups:
				groups = []
				groups.append(group_names)
				user_groups[user] = groups
			else:
				user_groups[user].append(group_names)
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"], "public":  ["admin", "userB"], "administrator": ["admin"] }))

# alternative way

def groups_per_user(group_dictionary):
    user_groups = {}
    for group, users in group_dictionary.items():
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
    return user_groups
print(groups_per_user({"local": ["admin", "userA"], "public":  ["admin", "userB"], "administrator": ["admin"] }))

#alternative get way

def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group,users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
        # Now add the group to the the list of
          # groups for this user, creating the entry
          # in the dictionary if necessary
          user_groups[user] = user_groups.get(user,[]) + [group]

    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
        "public":  ["admin", "userB"],
        "administrator": ["admin"] }))

#********************************************************************
# UPDATE

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)

# OUTPUT : {'shirt': ['red', 'blue', 'white'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}


# Question 5
# The add_prices function returns the total price of all of the groceries in the  dictionary.
# Fill in the blanks to complete this function.

def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for grocery, prices in basket.items():
      #  print(grocery, prices)
        total += prices
    return round(total, 2)
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?

    # Limit the return value to 2 decimal places
  #  return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
    "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

# 2.
# Question 2
# The highlight_word function changes the given word in a sentence to its upper-case version.
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day".
# Can you write this function in just one line?


def highlight_word(sentence, word):
    return(sentence.replace(word, word.upper()))


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


# 1.
# Question 1
#
# The format_address function separates out parts of the address string into new strings:
# house_number and street_name, and returns: "house number X on street named Y".
# The format of the input string is: numeric house number, followed by the street name which may contain numbers,
# but never by themselves, and could be several words long. For example, "123 Main Street",
# "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.


def format_address(address_string):
    # Declare variables
    house_number = int()

    # Separate the address string into parts
    address = address_string.split()
    # Traverse through the address parts
    for house_number in address:
        house_number = address[0]
        street_name = ' '.join(address[1:])

    # Determine if the address part is the
    # house number or part of the street name

    # Does anything else need to be done
    # before returning the result?

    # Return the formatted string
    return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

#3.
# Question 3
# A professor with two assistants, Jamie and Drew, the contents of Drew's list, followed by Jamie's list
# in reverse order, to get an accurate list of the students as they arrived.

def combine_lists(list1, list2):
 #   list1.reverse()
 #   list2.extend(list1)
    return list2 + list1[::-1]    # return list2
    # Generate a new list containing the elements of list2
    # Followed by the elements of list1 in reverse order
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

# 6.
# Question 6
# Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries,
# with names of their friends and how many guests each friend is bringing. Each dictionary is a partial list, but
# Rory's list has more current information about the number of guests. Fill in the blanks to combine
# both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary
# taking precedence, if a name is included in both dictionaries. Then print the resulting dictionary.
#

def combine_guests(guests1, guests2):
    for guest_name, friend in guests2.items():
        if guest_name in guests1:
            guests1[guest_name] = [guests1[guest_name], friend]     #[guests1[guestname], friend]
        else:
            guests1[guest_name] = friend

    return guests1

  # Combine both dictionaries into one, with each key listed
  # only once, and the value from guests1 taking precedence

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))
# ALTERNATIVE

#         if guest_name in guests1:
#             lst = []
#             friend_temp = guests1[guest_name]
#             lst.append(friend_temp)
#             lst.append(friend)
#             guests1[guest_name] = lst     #[guests1[guestname], friend]

# alternative

def combine_guests(guests1, guests2):
    party = {}
    for guest_name, friend in guests2.items():
        if guest_name in guests1:
            party[guest_name] = [guests1[guest_name], friend]
        else:
            party[guest_name] = friend
    for guest_name, friend in guests1.items():
        if guest_name not in guests2:
            party[guest_name] = friend

    return party

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))


# next question


def count_letters(text):
  result = {}
  text = text.lower()
  for letter in text:
    # Check if the letter needs to be counted or not
    if letter.isalpha():
      # Add or increment the value in the dictionary
      result[letter] = text.count(letter)

  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}