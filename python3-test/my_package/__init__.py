# Define package-level variables and functions
VERSION = '1.0.0'

def greet(name) :
    print(f"welcome {name}")

# import module in the __init__.py, it make them available to other modules in the packages
# Noted that the dot(.) before module1 indicates thats is a relative import
from .module1 import m1print
