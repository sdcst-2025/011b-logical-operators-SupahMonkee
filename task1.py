
#! python3
"""
The Earth maintains an orbit where it's closest distance to  
the sun is 0.9759 AU and it's furthest distance to the sun is 
1.016 AU. 
Mars maintans an orbit that has a minimum value of 1.524 AU and
a maximum value of 1.666 AU
Ask the user to enter a number. 
Tell them if the number is within Earth or Mars orbits
(2 points)

Inputs:
a number (float)

Outputs:
That is within normal Earth or Mars orbit.
That is not within normal Earth or Mars orbit.


Example:
Enter the distance from the sun in AU: 9.4
That is not within normal Earth or Mars orbit.

Enter the distance from the sun in AU: 1.011
That is within normal Earth or Mars orbit.

Enter the distance from the sun in AU: 1.6
That is within normal Earth or Mars orbit.

Enter the distance from the sun in AU: 2
That is not within normal Earth or Mars orbit.

"""
import math

x = float(input('Enter the distance from the sun in AU: '))

if (x > 0.9759 and x < 1.016) or (x > 1.524 and x < 1.666):
    print('That is within normal Earth or Mars orbit')
else:
    print('That is not within normal Earth or Mars orbit.')

#done