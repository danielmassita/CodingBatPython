"""
String-1 > extra_end
prev  |  next  |  chance
Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.


extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'
"""
 
def extra_end(str):
  if len(str) == 2:
    return str*3
  else:
    return (str[-2]+str[-1])*3
  
  """
  Expected	Run		
extra_end('Hello') → 'lololo'	'lololo'	OK	
extra_end('ab') → 'ababab'	'ababab'	OK	
extra_end('Hi') → 'HiHiHi'	'HiHiHi'	OK	
extra_end('Candy') → 'dydydy'	'dydydy'	OK	
extra_end('Code') → 'dedede'	'dedede'	OK	
other tests
OK	

All Correct

Our Solution:

def extra_end(str):
  end = str[-2:]
  return end + end + end
"""
