"""
String-1 > hello_name
prev  |  next  |  chance
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".


hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'
"""

def hello_name(name):
  return "Hello "+name+"!"

"""
Expected	Run		
hello_name('Bob') → 'Hello Bob!'	'Hello Bob!'	OK	
hello_name('Alice') → 'Hello Alice!'	'Hello Alice!'	OK	
hello_name('X') → 'Hello X!'	'Hello X!'	OK	
hello_name('Dolly') → 'Hello Dolly!'	'Hello Dolly!'	OK	
hello_name('Alpha') → 'Hello Alpha!'	'Hello Alpha!'	OK	
hello_name('Omega') → 'Hello Omega!'	'Hello Omega!'	OK	
hello_name('Goodbye') → 'Hello Goodbye!'	'Hello Goodbye!'	OK	
hello_name('ho ho ho') → 'Hello ho ho ho!'	'Hello ho ho ho!'	OK	
hello_name('xyz!') → 'Hello xyz!!'	'Hello xyz!!'	OK	
hello_name('Hello') → 'Hello Hello!'	'Hello Hello!'	OK	
other tests
OK	

All Correct
Our Solution:

def hello_name(name):
  return "Hello " + name + "!"

"""
