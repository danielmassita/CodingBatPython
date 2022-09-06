"""
String-1 > make_out_word
prev  |  next  |  chance
Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".


make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'
"""

def make_out_word(out, word):
  return out[0:2]+word+out[2:4]

"""
Expected	Run		
make_out_word('<<>>', 'Yay') → '<<Yay>>'	'<<Yay>>'	OK	
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'	'<<WooHoo>>'	OK	
make_out_word('[[]]', 'word') → '[[word]]'	'[[word]]'	OK	
make_out_word('HHoo', 'Hello') → 'HHHellooo'	'HHHellooo'	OK	
make_out_word('abyz', 'YAY') → 'abYAYyz'	'abYAYyz'	OK	
other tests
OK	

All Correct
"""
