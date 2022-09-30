"""
Warmup-2 > string_bits
prev  |  next  |  chance
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""

def string_bits(str):
  def string_bits(str):
  tamanho = len(str);
  return str[0:tamanho:2]

"""
Expected	Run		
string_bits('Hello') → 'Hlo'	'Hlo'	OK	
string_bits('Hi') → 'H'	'H'	OK	
string_bits('Heeololeo') → 'Hello'	'Hello'	OK	
string_bits('HiHiHi') → 'HHH'	'HHH'	OK	
string_bits('') → ''	''	OK	
string_bits('Greetings') → 'Getns'	'Getns'	OK	
string_bits('Chocoate') → 'Coot'	'Coot'	OK	
string_bits('pi') → 'p'	'p'	OK	
string_bits('Hello Kitten') → 'HloKte'	'HloKte'	OK	
string_bits('hxaxpxpxy') → 'happy'	'happy'	OK	

All Correct

Solution:
def string_bits(str):
  result = ""
  # Many ways to do this. This uses the standard loop of i on every char,
  # and inside the loop skips the odd index values.
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
  """
