
# Python Conditionals Examples

# Example 1: Simple if

# Check if a number is positive
num = 10

if num > 0:
    print("Example 1 Output: Number is positive")

# Notes:
# - Only one condition is checked.
# - If condition is True -> code inside runs.
# - If False -> nothing happens.


# Example 2: if-else
# Check if a number is positive or negative
num = -5

if num >= 0:
    print("Example 2 Output: Number is positive or zero")
else:
    print("Example 2 Output: Number is negative")

# Notes:
# - If condition is True -> first block runs.
# - If condition is False -> else block runs.


# Example 3: if-elif-else ladder
# Categorize a number as positive, zero, or negative
num = 0

if num > 0:
    print("Example 3 Output: Number is positive")
elif num == 0:
    print("Example 3 Output: Number is zero")
else:
    print("Example 3 Output: Number is negative")

# Notes:
# - Checks multiple conditions one after another.
# - First True condition's block will execute.
# - Remaining conditions are skipped.


# Example 4: Multiple independent if statements
# Check multiple independent conditions

num = 12

if num % 2 == 0:
    print("Example 4 Output: Number is even")

if num % 3 == 0:
    print("Example 4 Output: Number is divisible by 3")

if num % 4 == 0:
    print("Example 4 Output: Number is divisible by 4")

# Notes:
# - All conditions are checked separately.
# - More than one print can happen if multiple conditions are True.


# Example 5: if inside if (nested if)
# Check if a number is positive and even

num = 8

if num > 0:
    print("Example 5 Output: Number is positive")
    if num % 2 == 0:
        print("Example 5 Output: Number is even")

# Notes:
# - Nested if means an if statement inside another if.
# - The inner if runs only if the outer if is True.

# Quick Summary

"""
- Simple if: only checks 1 condition.
- if-else: choose between 2 options.
- if-elif-else: choose among multiple options.
- Multiple ifs: check multiple conditions separately.
- Nested ifs: if inside another if.
"""

