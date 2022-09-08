"""
List-1 > has23
prev  |  next  |  chance
Given an int array length 2, return True if it contains a 2 or a 3.


has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
"""

def has23(nums):
  if nums[0] == 2 or nums[1] == 2:
    return True
  elif nums[0] == 3 or nums[1] == 3:
    return True
  else:
    return False
  
  
def has23(nums):
  if nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3:
    return True
  else:
    return False

def has23(nums):
  return (nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3)

"""

Expected	Run		
has23([2, 5]) → True	True	OK	
has23([4, 3]) → True	True	OK	
has23([4, 5]) → False	False	OK	
has23([2, 2]) → True	True	OK	
has23([3, 2]) → True	True	OK	
has23([3, 3]) → True	True	OK	
has23([7, 7]) → False	False	OK	
has23([3, 9]) → True	True	OK	
has23([9, 5]) → False	False	OK	
other tests
OK	

All Correct
"""
