# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

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





