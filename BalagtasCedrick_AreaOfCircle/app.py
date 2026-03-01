import math

def BalagtasCircle():
    try:
        print("==========AREA OF A CIRCLE===========")
        BalagtasRadius = float(input("Enter the radius of the circle: "))
        print("-------------------------------------")
        BalagtasArea = math.pi * BalagtasRadius ** 2
        print("The area of the circle is:", BalagtasArea)
        print("=====================================")
        print("")
    except ValueError:
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
        print("       Enter a Numeric Value :P")
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

while True:
    BalagtasCircle()