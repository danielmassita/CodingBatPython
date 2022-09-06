"""
Logic-1 > caught_speeding
prev  |  next  |  chance
You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.


caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0
"""

def caught_speeding(speed, is_birthday):
  if is_birthday == True:
    speed -= 5
  if speed <= 61:
    return 0
  elif 61 < speed <= 80:
    return 1
  else:
    return 2
  
"""
Expected	Run		
caught_speeding(60, False) → 0	0	OK	
caught_speeding(65, False) → 1	1	OK	
caught_speeding(65, True) → 0	0	OK	
caught_speeding(80, False) → 1	1	OK	
caught_speeding(85, False) → 2	2	OK	
caught_speeding(85, True) → 1	1	OK	
caught_speeding(70, False) → 1	1	OK	
caught_speeding(75, False) → 1	1	OK	
caught_speeding(75, True) → 1	1	OK	
caught_speeding(40, False) → 0	0	OK	
caught_speeding(40, True) → 0	0	OK	
caught_speeding(90, False) → 2	2	OK	
other tests
OK	

All Correct
"""
