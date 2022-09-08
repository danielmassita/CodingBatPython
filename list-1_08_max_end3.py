"""
List-1 > max_end3
prev  |  next  |  chance
Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.


max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
"""

def max_end3(nums):
  if nums[0] == nums[2]:
    nums.append(nums[0])
    nums.append(nums[0])
    nums.append(nums[0])
    return nums[3:6]    
  elif nums[0] > nums[2]:
    nums.append(nums[0])
    nums.append(nums[0])
    nums.append(nums[0])
    return nums[3:6]
  elif nums[2] > nums[0]:
    nums.append(nums[2])
    nums.append(nums[2])
    nums.append(nums[2])
    return nums[3:6]
  
  """
  Expected	Run		
max_end3([1, 2, 3]) → [3, 3, 3]	[3, 3, 3]	OK	
max_end3([11, 5, 9]) → [11, 11, 11]	[11, 11, 11]	OK	
max_end3([2, 11, 3]) → [3, 3, 3]	[3, 3, 3]	OK	
max_end3([11, 3, 3]) → [11, 11, 11]	[11, 11, 11]	OK	
max_end3([3, 11, 11]) → [11, 11, 11]	[11, 11, 11]	OK	
max_end3([2, 2, 2]) → [2, 2, 2]	[2, 2, 2]	OK	
max_end3([2, 11, 2]) → [2, 2, 2]	[2, 2, 2]	OK	
max_end3([0, 0, 1]) → [1, 1, 1]	[1, 1, 1]	OK	
other tests
OK	

All Correct

def max_end3(nums):
  big = max(nums[0], nums[2])
  nums[0] = big
  nums[1] = big
  nums[2] = big
  return nums
"""
  
  
