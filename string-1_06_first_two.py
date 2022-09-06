"""
String-1 > first_two
prev  |  next  |  chance
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".


first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'
"""
  
def first_two(str):
  if len(str) == 0:
    return str
  elif len(str) < 2:
    return str
  else:
    return str[0]+str[1]

"""
Expected	Run		
first_two('Hello') → 'He'	'He'	OK	
first_two('abcdefg') → 'ab'	'ab'	OK	
first_two('ab') → 'ab'	'ab'	OK	
first_two('a') → 'a'	'a'	OK	
first_two('') → ''	''	OK	
first_two('Kitten') → 'Ki'	'Ki'	OK	
first_two('hi') → 'hi'	'hi'	OK	
first_two('hiya') → 'hi'	'hi'	OK	
other tests
OK	

All Correct
Our Solution:

def first_two(str):
  if len(str) >= 2:
    return str[:2]
  else:
    return str
"""
