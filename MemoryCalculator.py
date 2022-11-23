
from .test.test_memory_calculator import MemoryCalculator

class MemoryCalculator():
  
  def __init__(self, save_last_result=False):
    self._result = 0; self._save_last_result = save_last_result;
    
    self._last_result = None

  def add_number(self, number):
    self._result += number
    
  def multiply_number(self, number):
    if self._result == 0 and number != 0:
      self._result = 1*number
    else:
      self._result *= number  
      
  def subtract_number(self, number):
    self._result -= number    
  
  def get_result(self):
    temp = self._result
    return temp
  
  def get_last_result(self):
    temp = self._last_result
    return temp
  
  def reset_calculator(self):
    if self._save_last_result:
      self._last_result = self._result
    self._result = 0
