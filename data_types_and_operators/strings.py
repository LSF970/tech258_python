# Strings

single_quotes = 'Look! Single quotes'
double_quotes = "Look! Double Quotes"

print(single_quotes)
print(double_quotes)

# Generally prefer double quotes because ' can be used for other things

# bad_string = 'It's not right'
good_string = "It's not right"
print(good_string)

# If you really want to use single quotes
escape_example = 'I said \'Wow!\''
print(escape_example)

# String Indexing/Slicing

Hw = "Hello World!"

# Find out how many characters are in this string using an inbuilt python method
print(len(Hw))

# Target just the first character (H) using string indexing
print(Hw[0]) # Indexing starts at 0.

# Target the last character
print(Hw[11])
print(Hw[-1]) # better because it doesn't matter how long the string is

# Use negative indexing to get the second to last character (d)
print(Hw[-2]) # better because it doesn't matter how long the string is

# Bonus: Use string slicing to get the first 3 characters only
print(Hw[:3])

# String methods
White_space = "lot's of white space at the end                                                    "
print(len(White_space))
print(len(White_space.strip()))

example_string = "Here's some text with lot's of text"
# Count a substring within a string
print(example_string.count("text"))

# Make a string lowercase
print(example_string.lower())

# Make a string uppercase
print(example_string.upper())

# Make a string capitalised
print(example_string.capitalize())

# Replacing text
print(example_string.replace("with", ","))

# Concatenation and Casting

a = "here "
b = "more "
c = "much more"

# print(a + b + c)

x = 2
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"
w = "30"

print(str(x) + " " + str(y) + z)
print(x + y + int(w))

# F-strings

# name = "Lassie"
# years = 7
# height_cm = 60.2
#
# print(f"{name} is {years} years old and {height_cm} cm tall")

name = "Snoopy"
years = 52

print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS")

# using f-strings to format numbers

pi = 3.14159265359

# Use an f-string to print pi to 3 decimal places
print(f"The value of pi to 3 decimal places is {pi:.3}")


# Use an f-string to print pi to 5 decimal places
print(f"The value of pi to 5 decimal places is {pi:.5f}")

score = 16
max_score = 26

print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:%}")
print(f"You scored {score/max_score:.0%}")