"""
Logic-1 > sorta_sum
prev  |  next  |  chance
Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.


sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21
"""

def sorta_sum(a, b):
  sorta_sum = a + b
  if 10 <= sorta_sum <= 19:
    return 20
  else:
    return sorta_sum
    
"""
Expected	Run		
sorta_sum(3, 4) → 7	7	OK	
sorta_sum(9, 4) → 20	20	OK	
sorta_sum(10, 11) → 21	21	OK	
sorta_sum(12, -3) → 9	9	OK	
sorta_sum(-3, 12) → 9	9	OK	
sorta_sum(4, 5) → 9	9	OK	
sorta_sum(4, 6) → 20	20	OK	
sorta_sum(14, 7) → 21	21	OK	
sorta_sum(14, 6) → 20	20	OK	
other tests
OK	

All Correct

Our Solution:

def sorta_sum(a, b):
  sum = a + b
  if sum >= 10 and sum <= 19:
    return 20
  return sum
"""
