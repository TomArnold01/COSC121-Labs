def calculate_cartons(eggs):
    """ Calculate the number of cartons needed to hold 
        the specified number of eggs.
    """
    calculate_cartons = (eggs // 12)
    return(calculate_cartons)

print(calculate_cartons(65))