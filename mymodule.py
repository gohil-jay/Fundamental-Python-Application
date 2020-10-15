# User defined module for function
# To calculate the area of different shapes

def areaS(side):
    '''This function is to calculate the area of square shape with side as argument.'''
    a=side*side
    return a

def areaC(radius):
    '''This function is to calculate the area of circle shape with radius as argument.'''
    a=radius*radius*(22/7)
    return a

def areaR(length,breadth):
    '''This function is to calculate the area of rectangle shape with length and breadth as argument.'''
    a = (length*breadth)
    return a

def areaT(a,b,c):
    '''This function is to calculate the area of triangle shape with a(SIDE1) , b(SIDE2) and c(SIDE3) as argument.'''
    s=(a+b+c)/2
    Area=((s*(s-a)*(s-b)*(s-c))**(1/2))
    return Area
