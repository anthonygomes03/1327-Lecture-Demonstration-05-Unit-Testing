"""
Description: Module 05 demonstration: Functions with Unit Testing
Author: ACE Faculty
Date: {current date}
Usage: To execute the unit tests: 
        From the unit_testing directory in the Terminal:
        python -m unittest -v tests/test_functions.py
    To execute the python src program:
        From the unit_testing directory in the Terminal:
        python src/functions.py
"""


def greet_name_age(name: str, age: int)->str:
    """
    Returns a greeting which includes 
    the values of the name and age arguments.

    Args:
        name (str): The name of the person to greet.
        age (int): The age of the person to greet.
    
    Returns:
        str: A greeting including the argument values.
    """
    return f"Hello {name}, you are {age} years old!"

def grade_outcome(grade: int) -> str:
    """
    Provides a string outcome based on a grade argument.

    Args:
        grade (int): The earned grade.
    
    Returns:
        str: The string equivalent to the grade.
    """
    if grade > 90:
        output = "A+"
    elif grade >= 50:
        output = "Pass"
    else:
        output = "Fail"
    return output

def prompt_name_greeting()->str:
    """
    Prompts the user for their name and city, and 
    returns a phrase including both values.

    Args:
        name (int): The first operand.
        city (int): The second operand.
    Returns:
        str: A greeting with both argument values included.
    """
    name = input("Enter your name: ")
    city = input("Enter your current city: ")

    return f"Your name is {name} and your current city is {city}."



def math_operation(operand1: int, operand2: int, operation: str = "+")-> float:
    """
    Returns the result of the specified operation based 
    on the two operands.

    Args:
        operand1 (int): The first operand.
        operand2 (int): The second operand.
        operation (str): The operation to perform, default = "+"
    Returns:
        None
    Raises:
        ValueError:  "Invalid operation." When operation is not + or -.
        ValueError:  "ValueError" When a non-numeric operand is provided.
    """
    
    if operation == "+":
        result = operand1 + operand2
    elif operation == "-":
        result = operand1 - operand2
    else:
        raise ValueError("Invalid operation.")   
    
    return result

def integration()->None:
    print(math_operation(1, 2, "+"))
    print(prompt_name_greeting())

if __name__ == "__main__":
    integration()
