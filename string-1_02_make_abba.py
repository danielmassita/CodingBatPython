"""
String-1 > make_abba
prev  |  next  |  chance
Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".


make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'
"""

def make_abba(a, b):
  return (a+b)+(b+a)

"""
Expected	Run		
make_abba('Hi', 'Bye') → 'HiByeByeHi'	'HiByeByeHi'	OK	
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'	'YoAliceAliceYo'	OK	
make_abba('What', 'Up') → 'WhatUpUpWhat'	'WhatUpUpWhat'	OK	
make_abba('aaa', 'bbb') → 'aaabbbbbbaaa'	'aaabbbbbbaaa'	OK	
make_abba('x', 'y') → 'xyyx'	'xyyx'	OK	
make_abba('x', '') → 'xx'	'xx'	OK	
make_abba('', 'y') → 'yy'	'yy'	OK	
make_abba('Bo', 'Ya') → 'BoYaYaBo'	'BoYaYaBo'	OK	
make_abba('Ya', 'Ya') → 'YaYaYaYa'	'YaYaYaYa'	OK	
other tests
OK	

All Correct

Our Solution:

def make_abba(a, b):
  return a + b + b + a
  
"""
