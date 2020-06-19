#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This would be linear because the time it takes for this to run willvary dependening on the value of a.  If a is large then it will take longer.


b) The run time for this would be quadratic due to the nested loops.


c) The run time for this would be constant because the operation time would always be the same even depending on the value of bunnies.

## Exercise II
 


# I would lke to make the following assumptions:
  # If an egg doesn’t break when dropped from some floor, then it will not break when dropped from any lower floors.
  # An egg that survives a fall can be used again.
  # The effect of a fall is the same for all eggs.
  # If an egg breaks when dropped, then it would break if dropped from a higher floor.

# The simplest answer would be to throw the egg off of the first floor and then move to the second and so on until 
# the egg finally broke.  This would be very reliable but expensive because there is a posibility it could take 100 
# throws if there are 100 floors.

# We could also throw the egg from 1/3 of the way up the bulding using the first egg and if it breaks we go down 1/3 
# of the way and test it with the second egg.  This is all subjective to the amount of floors there are so if you had
# 100 floors for example it could take  up to 33 eggs.

# Time complexity would be O(n2) or quadratic, because there is a case of overlapping sub-problems the time complexity is exponential.  It isn't contstant because the time would vary on the amount of floors.