# Function Parameter Passing in Python
# 1. Positional Arguments
# 1. Positional Arguments
# 2. Keyword Arguments
# 3. Default Arguments
# 4. Variable-Length Positional Arguments (*args)
# 5. Variable-Length Keyword Arguments (**kwargs)
# 6. Combination of All Types

def greet1(name, message):
    print(f"Positional -> Hello {name}, {message}")

greet1("Omkar", "Good Morning")  # Arguments passed by position

# The first argument goes to 'name', second to 'message'.

# 2. Keyword Arguments
def greet2(name, message):
    print(f"Keyword -> Hello {name}, {message}")

greet2(message="Hi there", name="Bob")  # Arguments passed by name

# You can change the order when using keyword arguments.

# 3. Default Arguments
def greet3(name, message="Welcome!"):
    print(f"Default -> Hello {name}, {message}")

greet3("Charlie")              # Uses default message
greet3("David", "Good Day")    # Overrides default message

# If 'message' is not provided, it uses the default value.


# 4. Variable-Length Positional Arguments (*args)
def sum_numbers(*args):
    print(f"*args -> You passed: {args}")
    print("Sum =", sum(args))

sum_numbers(1, 2, 3)
sum_numbers(10, 20, 30, 40)

# '*args' collects all extra positional arguments as a tuple.

# 5. Variable-Length Keyword Arguments (**kwargs)
def print_info(**kwargs):
    print("**kwargs -> Info received:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_info(name="Eva", age=30, city="Delhi")

# '**kwargs' collects all keyword arguments into a dictionary.

# 6. Combination of All Types
def full_example(a, b=2, *args, **kwargs):
    print(f"a = {a}, b = {b}")
    print("Additional positional (*args):", args)
    print("Additional keyword (**kwargs):", kwargs)

full_example(10, 20, 30, 40, x=100, y=200)
