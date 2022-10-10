# Question 1
# Fill in the blanks of this code to print out the numbers 1 through 7.

number = 1
while number ___ 7:
    print(number, end=" ")
    ___


# Question 2
# The show_letters function should print out each letter of a word on a separate line. Fill in the blanks to make that happen.

def show_letters(word):
    for __:
        print(__)

show_letters("Hello")
# Should print one line per letter

# Question 3
# Complete the function digits(n) that returns how many digits the number has.
# For example: 25 has 2 digits and 144 has 3 digits.
# Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.

def digits(n):
    count = 0
    if n == 0:
        ___
    while (___):
        count += 1
        ___
    return count


print(digits(25))  # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))  # Should print 1



# Question 5
# The counter function counts down from start to stop when start is bigger than stop,
# and counts up from start to stop otherwise. Fill in the blanks to make this work correctly.

def counter(start, stop):
    x = start
    if ___:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if ___:
                return_string += ","
            ___
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if ___:
                return_string += ","
            ___
    return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

# Question 8
# What is the value of x at the end of the following code?

for x in range(1, 10, 3):
    print(x)

# Question 9
# What is the value of y at the end of the following code?

for x in range(10):
    for y in range(x):
        print(y)


# 7 , 8

# 6.Question 6
#The loop function is similar to range(), but handles the parameters somewhat differently: it takes in 3 parameters:
# the starting point, the stopping point, and the increment step. When the starting point is greater
#than the stopping point, it forces the steps to be negative. When, instead, the starting point is less
#than the stopping point, it forces the step to be positive. Also, if the step is 0, it changes to 1 or -1.
#The result is returned as a one-line, space-separated string of numbers. For example, loop(11,2,3)
#should return 11 8 5 and loop(1,5,0) should return 1 2 3 4. Fill in the missing parts to make that happen.
#"""

def loop(start, stop, step):
    return_string = ""
    if step == 0:
        step=1
    if start>stop:
        step = abs(step) * -1
    else:
        step = abs(step)
    for count in range(start, stop, step):
        return_string += str(count) + " "
    return return_string.strip()

print(loop(11,2,3)) # Should be 11 8 5
print(loop(1,5,0)) # Should be 1 2 3 4
print(loop(-1,-2,0)) # Should be -1
print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24
print(loop(1,1,1)) # Should be empty