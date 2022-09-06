"""
String-1 > make_tags
prev  |  next  |  chance
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".


make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'
"""

def make_tags(tag, word):
  return '<'+tag+'>'+word+'</'+tag+'>'

"""
Expected	Run		
make_tags('i', 'Yay') → '<i>Yay</i>'	'<i>Yay</i>'	OK	
make_tags('i', 'Hello') → '<i>Hello</i>'	'<i>Hello</i>'	OK	
make_tags('cite', 'Yay') → '<cite>Yay</cite>'	'<cite>Yay</cite>'	OK	
make_tags('address', 'here') → '<address>here</address>'	'<address>here</address>'	OK	
make_tags('body', 'Heart') → '<body>Heart</body>'	'<body>Heart</body>'	OK	
make_tags('i', 'i') → '<i>i</i>'	'<i>i</i>'	OK	
make_tags('i', '') → '<i></i>'	'<i></i>'	OK	
other tests
OK	

All Correct
"""
