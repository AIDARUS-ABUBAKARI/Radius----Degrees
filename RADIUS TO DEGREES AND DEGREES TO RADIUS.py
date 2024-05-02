while True:

  import math
  
  name = int(input("RADIUS to DEGREES press 5   or DEGREES to RADIUS press 2: 8 to quit:   "))
  if name == 2:
    user = float(input("Enter the degreea: "))
    radius = user*math.pi/180
    print("Your radius is: ", radius)
 

  elif name == 5:
    num = float(input("Enter the radius: "))
    degrees = num*180/math.pi
    print("Your degrees is: ", degrees)

  else:
    print("Have a good day")
    break

