"""
Logic-1 > cigar_party
prev  |  next  |  chance
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.


cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True
"""

def cigar_party(cigars, is_weekend):
  if is_weekend == True and cigars >= 40:
    return True
  elif is_weekend == False and 40 <= cigars <= 60:
    return True
  else:
    return False
    
"""
Expected	Run		
cigar_party(30, False) → False	False	OK	
cigar_party(50, False) → True	True	OK	
cigar_party(70, True) → True	True	OK	
cigar_party(30, True) → False	False	OK	
cigar_party(50, True) → True	True	OK	
cigar_party(60, False) → True	True	OK	
cigar_party(61, False) → False	False	OK	
cigar_party(40, False) → True	True	OK	
cigar_party(39, False) → False	False	OK	
cigar_party(40, True) → True	True	OK	
cigar_party(39, True) → False	False	OK	
other tests
OK	

All Correct

Our Solution:

def cigar_party(cigars, is_weekend):
  if is_weekend:
    return (cigars >= 40)
  else:
    return (cigars >= 40 and cigars <= 60)
"""
