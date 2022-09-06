"""
Logic-1 > squirrel_play
prev  |  next  |  chance
The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.


squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True
"""

def squirrel_play(temp, is_summer):
  if is_summer == True and 60 <= temp <= 100:
    return True
  elif 60 <= temp <= 90:
    return True
  else:
    return False

"""
Expected	Run		
squirrel_play(70, False) → True	True	OK	
squirrel_play(95, False) → False	False	OK	
squirrel_play(95, True) → True	True	OK	
squirrel_play(90, False) → True	True	OK	
squirrel_play(90, True) → True	True	OK	
squirrel_play(50, False) → False	False	OK	
squirrel_play(50, True) → False	False	OK	
squirrel_play(100, False) → False	False	OK	
squirrel_play(100, True) → True	True	OK	
squirrel_play(105, True) → False	False	OK	
squirrel_play(59, False) → False	False	OK	
squirrel_play(59, True) → False	False	OK	
squirrel_play(60, False) → True	True	OK	
other tests
OK	

All Correct

"""
