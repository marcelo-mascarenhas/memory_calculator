import unittest
from MemoryCalculator import MemoryCalculator

class TestMemoryCalculator(unittest.TestCase):

  def test_sum_is_zero_on_initialization(self):
    calculator = MemoryCalculator()
    self.assertEqual(0, calculator.get_result())

  def test_sum_one_number(self):
    calculator = MemoryCalculator()
    calculator.add_number(37); 
    self.assertEqual(37, calculator.get_result())


  def test_sum_two_numbers(self):
    calculator = MemoryCalculator()
    calculator.add_number(37);
    calculator.add_number(13)
    self.assertEqual(50, calculator.get_result())
  
  def test_multiplication_of_two_numbers(self):
    calculator = MemoryCalculator()
    calculator.multiply_number(2);
    calculator.multiply_number(4);

    self.assertEqual(8, calculator.get_result())
    
  
  def test_subtraction_of_number(self):
    calculator = MemoryCalculator()
    calculator.subtract_number(10);

    self.assertEqual(-10, calculator.get_result())


  def test_last_result(self):
    calculator = MemoryCalculator(True)
    calculator.multiply_number(2); calculator.subtract_number(4);
    calculator.reset_calculator();

    self.assertEqual(-2, calculator.get_last_result())

  def test_cleaned_result_after_reset(self):
    calculator = MemoryCalculator(True)
    calculator.multiply_number(2); calculator.subtract_number(4);
    calculator.reset_calculator();

    self.assertEqual(0, calculator.get_result())
