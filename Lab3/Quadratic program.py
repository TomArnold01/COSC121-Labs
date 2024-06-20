""" Input a, b, c parameters from the user and 
calculate the quadractic"""

import math

def print_quad(a, b, c):
    """print the root of the quad for a, b, c"""
    
    if a== 0:
        print("not a Quadratic")
    else:
        discr = b ** 2 - 4 * a * c
        if discr >= 0:
            root1 = (-b - math.sqrt(discr)) / (2 * a)
            root2 = (-b + math.sqrt(discr)) / (2 * a)
            print("solution: {:.4f}, {:.4f}".format(root1, root2))
        else:
            print("Roots are imaginary")

def get_quad_params():
    """promt user and call print_quad"""
    a = float(input("Vaule for a: "))
    b = float(input("Vaule for b: "))
    c = float(input("Vaule for c: "))
    print_quad(a, b, c)
    
get_quad_params()