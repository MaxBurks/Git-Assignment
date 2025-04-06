#Function 1
#Returns Area of square

#Written by Max
def rect_area(side):
    '''

    This function calculates the area of a rectangle
    
    Parameters
    ----------
    int: length
    int: width
    
    Return
    ------
    length*width
    
    '''
    return(side**2)

#Function 2
#Returns Surface Area of Cubic Prism
#written by Osvaldo Contreras-Guzman
def rect_surface_area(square):
    """
    Calculates the surface area of a cube by multiplying square by 6

    Returns
    -------
    int : surface area of cube
    """
    return square * 6


#Request the dimensions of a solid square object
side = int(input("Enter the length of the side of the cube as a integer: "))

square = rect_area(side)  
print("Side =", side)
print("Total Surface Area = ", str(rect_surface_area(square)))
print("Area of the square: ", str(rect_area(side)))


