"""
String-1 > combo_string
prev  |  next  |  chance
Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).


combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'
"""

def combo_string(a, b):
  if len(a) > len(b):
    return b+a+b
  elif len(b) > len(a):
    return a+b+a
  
"""
Expected	Run		
combo_string('Hello', 'hi') → 'hiHellohi'	'hiHellohi'	OK	
combo_string('hi', 'Hello') → 'hiHellohi'	'hiHellohi'	OK	
combo_string('aaa', 'b') → 'baaab'	'baaab'	OK	
combo_string('b', 'aaa') → 'baaab'	'baaab'	OK	
combo_string('aaa', '') → 'aaa'	'aaa'	OK	
combo_string('', 'bb') → 'bb'	'bb'	OK	
combo_string('aaa', '1234') → 'aaa1234aaa'	'aaa1234aaa'	OK	
combo_string('aaa', 'bb') → 'bbaaabb'	'bbaaabb'	OK	
combo_string('a', 'bb') → 'abba'	'abba'	OK	
combo_string('bb', 'a') → 'abba'	'abba'	OK	
combo_string('xyz', 'ab') → 'abxyzab'	'abxyzab'	OK	
other tests
OK	

All Correct
"""
