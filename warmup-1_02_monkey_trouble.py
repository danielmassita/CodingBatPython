"""
monkey_trouble
prev  |  next  |  chance
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.


monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
"""

def monkey_trouble(a_smile, b_smile):
  if (a_smile == True and b_smile == True):
    return True
  elif (a_smile == False and b_smile == False):
    return True
  elif (a_smile == True and b_smile == False):
    return False
  elif (a_smile == False and b_smile == True):
    return False
  
"""
Expected	Run		
monkey_trouble(True, True) → True	True	OK	
monkey_trouble(False, False) → True	True	OK	
monkey_trouble(True, False) → False	False	OK	
monkey_trouble(False, True) → False	False	OK	

All Correct

Solution:
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False
  ## The above can be shortened to:
  ##   return ((a_smile and b_smile) or (not a_smile and not b_smile))
  ## Or this very short version (think about how this is the same as the above)
  ##   return (a_smile == b_smile)
  """
