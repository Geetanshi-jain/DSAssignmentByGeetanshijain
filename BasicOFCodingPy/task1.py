# Basics of Python Coding
## 1. Using Comments in Python
# Single-line comments
# This is a single-line comment
# Multi-line comments (using triple quotes)
"""
This is a multi-line comment
or docstring.
"""
## 2. Executing Commands in Python
# Commands are executed line by line in Python scripts or interactive consoles
print("Hello, Python!")  # Print a statement
result = 2 + 3           # Perform a calculation
print(result)            # Output the result
## 3. Importing Packages in Python
# To use external libraries in Python, you need to import them
import math               # Import a standard library module
from datetime import datetime  # Import specific parts of a module
print(math.sqrt(16))       # Using a function from the math package
print(datetime.now())      # Get the current date and time
## 4. Getting Data into Python
# You can get data into Python in many ways, such as reading from files or using libraries like pandas for structured data
# Reading from a file
with open('data.txt', 'r') as file:
    data = file.read()
print(data)
# Reading CSV files using pandas
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())  # Show the first few rows of the data
## 5. Saving Output in Python
# Saving text to a file
output = "Hello, Python!"
with open('output.txt', 'w') as file:
    file.write(output)
# Saving data using pandas
df.to_csv('output.csv', index=False)  # Save DataFrame as CSV
## 6. Accessing Records and Variables in Python
# Lists (accessing elements)
my_list = [10, 20, 30, 40]
print(my_list[0])  # Access the first element (index 0)
# Dictionaries (accessing key-value pairs)
my_dict = {'name': 'John', 'age': 30}
print(my_dict['name'])  # Access value by key
# DataFrames (accessing rows/columns)
df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})
print(df['name'])       # Access a column
print(df.iloc[0])      # Access the first row
