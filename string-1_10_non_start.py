"""
String-1 > non_start
prev  |  next  |  chance
Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.


non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'
"""

def non_start(a, b):
  return a[1:]+b[1:]

"""
Expected	Run		
non_start('Hello', 'There') → 'ellohere'	'ellohere'	OK	
non_start('java', 'code') → 'avaode'	'avaode'	OK	
non_start('shotl', 'java') → 'hotlava'	'hotlava'	OK	
non_start('ab', 'xy') → 'by'	'by'	OK	
non_start('ab', 'x') → 'b'	'b'	OK	
non_start('x', 'ac') → 'c'	'c'	OK	
non_start('a', 'x') → ''	''	OK	
non_start('kit', 'kat') → 'itat'	'itat'	OK	
non_start('mart', 'dart') → 'artart'	'artart'	OK	
other tests
OK	

All Correct
"""
