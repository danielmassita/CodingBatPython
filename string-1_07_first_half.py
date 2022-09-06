"""
String-1 > first_half
prev  |  next  |  chance
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'
"""
      
def first_half(str):
  tamanho = len(str)
  metadeTamanho = tamanho/2
  if tamanho == 0:
    return ""
  elif tamanho == 2:
    return str[0]
  elif tamanho == 4:
    return str[0]+str[1]
  else:
    for i in range(metadeTamanho):
      return str[i:metadeTamanho]
      
"""
Expected	Run		
first_half('WooHoo') → 'Woo'	'Woo'	OK	
first_half('HelloThere') → 'Hello'	'Hello'	OK	
first_half('abcdef') → 'abc'	'abc'	OK	
first_half('ab') → 'a'	'a'	OK	
first_half('') → ''	''	OK	
first_half('0123456789') → '01234'	'01234'	OK	
first_half('kitten') → 'kit'	'kit'	OK	
other tests
OK	

All Correct
"""
