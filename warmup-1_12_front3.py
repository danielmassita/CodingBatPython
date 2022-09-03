"""
Warmup-1 > front3
prev  |  next  |  chance
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.


front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""

def front3(str):
  tamanho = len(str)
  if tamanho < 3:
    return str*3
  else:
    return str[0:3]*3
  
"""
Expected	Run		
front3('Java') → 'JavJavJav'	'JavJavJav'	OK	
front3('Chocolate') → 'ChoChoCho'	'ChoChoCho'	OK	
front3('abc') → 'abcabcabc'	'abcabcabc'	OK	
front3('abcXYZ') → 'abcabcabc'	'abcabcabc'	OK	
front3('ab') → 'ababab'	'ababab'	OK	
front3('a') → 'aaa'	'aaa'	OK	
front3('') → ''	''	OK	

All Correct

Solution:
def front3(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front 
  
  # Could omit the if logic, and write simply front = str[:3]
  # since the slice is silent about out-of-bounds conditions.
  
"""
