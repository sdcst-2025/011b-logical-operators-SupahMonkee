#!python3
'''
Note that a logical operation is just like nesting or adding conditional statements inside a conditional statement:
'''

x = 3
y = 4

'''
the following 2 statements produce the same result
'''

if x==3 and y == 4:
  print("this result is true")
 

if x == 3:
  if y == 4:
    print("this is the same result")
  
  
'''
the following 2 statements are identical
'''
if x == 3:
  print("this is the second result")
if y == 5:
  print("this is the second result")

if x ==3 or y==5:
  print("this is the second result")
  
