# Higher-order function that takes a function as a parameter
def apply_operation(operation, x, y):
    return operation(x, y)

# Closure: Returns a function that multiplies by a specific factor
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

# Side-effect-free function: Pure function that calculates the square of a number
def square(x):
    return x ** 2

# Anonymous function: Lambda function to calculate the sum of two numbers
sum_function = lambda a, b: a + b

# Final data structure: List comprehension to create a list of squares
numbers = [1, 2, 3, 4, 5]
squares = [square(x) for x in numbers]

# Using higher-order function to apply the sum_function
result = apply_operation(sum_function, 10, 5)

# Using closure to create a multiplier function and applying it
double = multiplier(2)
triple = multiplier(3)

# Examples
print("List of squares:", squares)
print("Sum of 10 and 5:", result)
print("Double of 7:", double(7))
print("Triple of 5:", triple(5))

