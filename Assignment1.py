# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    maxnum = max(num1, num2, num3)
    return maxnum

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    minnum = min(num1, num2, num3)
    return minnum

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    if number == 0:
        number = "Zero"
    elif number > 0:
        number = "Positive"
    elif number < 0:
        number = "Negative"
    return number

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows): 
    star = ""
    for x in range(rows): 
        star += ("*" * (x+1) + "\n")
    return star.rstrip()
 

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    return
    

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    # TODO: Implement this function
    pass  # Replace with your code
