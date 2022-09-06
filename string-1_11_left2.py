"""
String-1 > left2
prev  |  next  |  chance
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.


left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'
"""

def left2(str):
  tamanhoString = len(str)
  if tamanhoString == 2:
    return str
  elif tamanhoString > 2:
    return str[2:]+str[0:2]
  
"""
Expected	Run		
left2('Hello') → 'lloHe'	'lloHe'	OK	
left2('java') → 'vaja'	'vaja'	OK	
left2('Hi') → 'Hi'	'Hi'	OK	
left2('code') → 'deco'	'deco'	OK	
left2('cat') → 'tca'	'tca'	OK	
left2('12345') → '34512'	'34512'	OK	
left2('Chocolate') → 'ocolateCh'	'ocolateCh'	OK	
left2('bricks') → 'icksbr'	'icksbr'	OK	
other tests
OK	

All Correct
Our Solution:

def left2(str):
  return str[2:] + str[:2]
"""
