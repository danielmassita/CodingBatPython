"""
List-1 > same_first_last
prev  |  next  |  chance
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.


same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
"""

def same_first_last(nums):
  tamanho = len(nums)
  return tamanho >= 1 and (nums[0] == nums[-1])

"""
Expected	Run		
same_first_last([1, 2, 3]) → False	False	OK	
same_first_last([1, 2, 3, 1]) → True	True	OK	
same_first_last([1, 2, 1]) → True	True	OK	
same_first_last([7]) → True	True	OK	
same_first_last([]) → False	False	OK	
same_first_last([1, 2, 3, 4, 5, 1]) → True	True	OK	
same_first_last([1, 2, 3, 4, 5, 13]) → False	False	OK	
same_first_last([13, 2, 3, 4, 5, 13]) → True	True	OK	
same_first_last([7, 7]) → True	True	OK	
other tests
OK	

All Correct
Our Solution:

def same_first_last(nums):
  return (len(nums) >= 1 and nums[0] == nums[-1])
"""
