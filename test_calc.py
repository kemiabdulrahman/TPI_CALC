import Function
import unittest
from unittest.mock import patch
from io import StringIO
import sys

class CalcTestCase(unittest.TestCase):
    @patch('builtins.input', side_effect=['2 + 2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_input(self, mock_stdout, mock_input):
        Function.calc()
        self.assertEqual(mock_stdout.getvalue().strip(), '4')

    @patch('builtins.input', side_effect=['1 / 0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_zero_division_error(self, mock_stdout, mock_input):
        Function.calc()
        self.assertEqual(
            mock_stdout.getvalue().strip(), "can't divide by zero"
        )

    @patch('builtins.input', side_effect=['6 * '])
    @patch('sys.stdout', new_callable=StringIO)
    def test_syntax_error(self, mock_stdout, mock_input):
        Function.calc()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Syntax Error')

    @patch('builtins.input', side_effect=['undefined_variable'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_name_error(self, mock_stdout, mock_input):
        Function.calc()
        self.assertEqual(mock_stdout.getvalue().strip(), 'NameError')

    @patch('builtins.input', side_effect=['2 + "4"'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_type_error(self, mock_stdout, mock_input):
        Function.calc()
        self.assertEqual(mock_stdout.getvalue().strip(), 'OperatorError')

if __name__ == '__main__':
    unittest.main()