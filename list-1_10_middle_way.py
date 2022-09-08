"""
List-1 > middle_way
prev  |  next  |  chance
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.


middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]
"""

def middle_way(a, b):
  doMeioA = a[1]
  doMeioB = b[1]
  novaLista = [doMeioA, doMeioB]
  return novaLista

"""
Expected	Run		
middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]	[2, 5]	OK	
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]	[7, 8]	OK	
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]	[2, 4]	OK	
middle_way([1, 9, 7], [4, 8, 8]) → [9, 8]	[9, 8]	OK	
middle_way([1, 2, 3], [3, 1, 4]) → [2, 1]	[2, 1]	OK	
middle_way([1, 2, 3], [4, 1, 1]) → [2, 1]	[2, 1]	OK	
other tests
OK	

All Correct
"""
