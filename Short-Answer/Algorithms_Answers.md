#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) If we divide n^3 by n^2 = n.  So the Big O would be constant, O(1), because the number of operations is constant.


b) This will be Logarithmic O(log n), because as the sixe of the input increases the runtime and space used will grow at a slghtly slower rat.


c) This will be Exponential, O(c^n), because as the size of the input increases the runtime or space used will grow at a much faster rate.

## Exercise II

- I would like to use the binary search to utilize the 'halfing' concept to find the highest floor that can be dropped from without breaking.  

- First I would create and store variables such as 'top' 'mid' and 'bottom'.  

- I would begin every simulation by finding the 'mid' and I could so that by adding the 'top' and 'bottom' and // 2.

-  Once the 'mid' is found I would then drop the egg from the 'mid'.  If the egg broke I know I would need to go down floors.  So I woould make the 'mid' = top and 'bottom' would stay the same and I would calculate the 'mid' recursively and run the entire fall and move recursivley until we find the point where the egg did not break right below the final floor.

- The run time for this solutions would be Logarithmic, O(log n).