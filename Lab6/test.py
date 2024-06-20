def input_and_print_rectangle():
    """ get the parpmeters and prints the area"""
    width = input("Rectangle width? ")
    height = input("Rectangle height? ")
    area = float(width) * float(height)
    area1 = "{:.2f}".format(area)

    print("The area of the rectangle is: " + str(area1))

input_and_print_rectangle()