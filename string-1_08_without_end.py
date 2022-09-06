"""
String-1 > without_end
prev  |  next  |  chance
Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.


without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'
"""
def without_end(str):
  return str[1:-1]

"""
Expected	Run		
without_end('Hello') → 'ell'	'ell'	OK	
without_end('java') → 'av'	'av'	OK	
without_end('coding') → 'odin'	'odin'	OK	
without_end('code') → 'od'	'od'	OK	
without_end('ab') → ''	''	OK	
without_end('Chocolate!') → 'hocolate'	'hocolate'	OK	
without_end('kitten') → 'itte'	'itte'	OK	
without_end('woohoo') → 'ooho'	'ooho'	OK	
other tests
OK	

All Correct
"""
