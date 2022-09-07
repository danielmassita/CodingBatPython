"""
Logic-1 > in1to10
prev  |  next  |  chance
Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.


in1to10(5, False) → True
in1to10(11, False) → False
in1to10(11, True) → True
"""

def in1to10(n, outside_mode):
  if outside_mode == True and (n <= 1 or n >= 10):
    return True
  elif outside_mode == False and (1 <= n <= 10):
    return True
  else:
    return False
  
"""
Expected	Run		
in1to10(5, False) → True	True	OK	
in1to10(11, False) → False	False	OK	
in1to10(11, True) → True	True	OK	
in1to10(10, False) → True	True	OK	
in1to10(10, True) → True	True	OK	
in1to10(9, False) → True	True	OK	
in1to10(9, True) → False	False	OK	
in1to10(1, False) → True	True	OK	
in1to10(1, True) → True	True	OK	
in1to10(0, False) → False	False	OK	
in1to10(0, True) → True	True	OK	
in1to10(-1, False) → False	False	OK	
in1to10(-1, True) → True	True	OK	
in1to10(99, False) → False	False	OK	
in1to10(-99, True) → True	True	OK	
other tests
OK	

All Correct
"""
