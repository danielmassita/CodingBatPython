"""
Logic-1 > near_ten
prev  |  next  |  chance
Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod


near_ten(12) → True
near_ten(17) → False
near_ten(19) → True
"""

def near_ten(num):
  if (num % 10 <= 2) or (num % 10 >= 8):
    return True
  else:
    return False
  
"""
Expected	Run		
near_ten(12) → True	True	OK	
near_ten(17) → False	False	OK	
near_ten(19) → True	True	OK	
near_ten(31) → True	True	OK	
near_ten(6) → False	False	OK	
near_ten(10) → True	True	OK	
near_ten(11) → True	True	OK	
near_ten(21) → True	True	OK	
near_ten(22) → True	True	OK	
near_ten(23) → False	False	OK	
near_ten(54) → False	False	OK	
near_ten(155) → False	False	OK	
near_ten(158) → True	True	OK	
near_ten(3) → False	False	OK	
near_ten(1) → True	True	OK	
other tests
OK	

All Correct
"""
