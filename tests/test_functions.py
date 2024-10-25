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

import unittest
from unittest.mock import patch
from src.functions import greet_name_age, grade_outcome, prompt_name_greeting, math_operation

class TestFunctions(unittest.TestCase):
    def test_greet_name_with_all_parameters(self):
        # Arrange
        name = "Joe"
        age = 25
        expected = "Hello Joe, you are 25 years old!" 

        # Act
        actual = greet_name_age(name, age) 

        # Assert
        self.assertEqual(expected, actual)


    def test_grade_outcome_a_plus(self):
        # Arrange
        grade = 91
        expected = "A+"

        # Act
        actual = grade_outcome(grade)

        # Assert
        self.assertEqual(expected, actual)

    def test_grade_outcome_pass(self):
        # Arrange
        grade = 76
        low_edge = 50
        high_edge = 90
        expected = "Pass"

        # Act
        # COMMENT OUT WITH EDGE CASES actual = grade_outcome(grade)

        # Act and Assert including edge cases
        self.assertEqual(expected, grade_outcome(grade))
        self.assertEqual(expected, grade_outcome(low_edge))
        self.assertEqual(expected, grade_outcome(high_edge))



    def test_grade_outcome_fail(self):
        # Arrange
        grade = 40
        high_edge = 49
        negative = -1
        expected = "Fail"

        # Act and Assert including edge cases
        self.assertEqual(expected, grade_outcome(grade))
        self.assertEqual(expected, grade_outcome(high_edge))
        self.assertEqual(expected, grade_outcome(negative))

    def prompt_name_greeting_correct_output(self):
        # builtins.input <-- allows us to  mock input
        # builtins.print <-- would allow us to mock print
        with patch('builtins.input') as mock_input:
            # Arrange
            # The side_effect list below 'mocks' input values that
            # are prompted for in the function:
            mock_input.side_effect = ["Joe", "Winnipeg"]
            expected = "Hello Joe, you are from Winnipeg!"

            # Act (act within the patch context)
            actual = prompt_name_greeting()

            # Assert
            self.assertEqual(expected, actual)

    def test_math_operation_successful_addition(self):
        # Arrange
        operand1 = 10
        operand2 = 20
        operator = "+"
        expected = 30

        # Act
        actual = math_operation(operand1, operand2, operator)

        # Assert
        self.assertEqual(expected, actual)

    def test_math_operation_successful_subtraction(self):
        # Arrange
        operand1 = 30
        operand2 = 20
        operator = "-"
        expected = 10

        # Act
        actual = math_operation(operand1, operand2, operator)

        # Assert
        self.assertEqual(expected, actual)


        def test_math_operation_bad_operator_raises_exception(self):
            # Arrange
            operand1 = 30
            operand2 = 20
            operator = "*"
            expected = "Invalid operation."

            # Act and Assert
            # assertRaises(ValueError) <-- because function raises 
            # ValueError when an invalid operator is provided
            with self.assertRaises(ValueError) as context:
                math_operation(operand1, operand2, operator)
            
            self.assertEqual(expected, str(context.exception))


        def test_math_operation_non_numeric_operand_raises_exception(self):
            # Arrange
            operand1 = "30"
            operand2 = 20
            operator = "-"

            # Act and Assert
            # assertRaises(ValueError) <-- because function raises 
            # ValueError when an invalid operator is provided
            with self.assertRaises(ValueError) as context:
                math_operation(operand1, operand2, operator)
            
            # In this case, we don't control the exception message
            # because it is not raised explicitly by the programmer
            # Therefore, no assert for the error message.
