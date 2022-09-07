"""
Logic-1 > love6
prev  |  next  |  chance
The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.


love6(6, 4) → True
love6(4, 5) → False
love6(1, 5) → True
"""

def love6(a, b):
  if a == 6 or b == 6:
    return True
  elif a + b == 6 or a - b == 6 or b - a == 6:
    return True
  else:
    return False
  
"""
Expected	Run		
love6(6, 4) → True	True	OK	
love6(4, 5) → False	False	OK	
love6(1, 5) → True	True	OK	
love6(1, 6) → True	True	OK	
love6(1, 8) → False	False	OK	
love6(1, 7) → True	True	OK	
love6(7, 5) → False	False	OK	
love6(8, 2) → True	True	OK	
love6(6, 6) → True	True	OK	
love6(-6, 2) → False	False	OK	
love6(-4, -10) → True	True	OK	
love6(-7, 1) → False	False	OK	
love6(7, -1) → True	True	OK	
love6(-6, 12) → True	True	OK	
love6(-2, -4) → False	False	OK	
love6(7, 1) → True	True	OK	
love6(0, 9) → False	False	OK	
love6(8, 3) → False	False	OK	
love6(3, 3) → True	True	OK	
love6(3, 4) → False	False	OK	
other tests
OK	

All Correct
"""
