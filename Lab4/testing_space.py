def vertical_strings(string):
    """take a string as a parameter and prints each letter of all the string
    on a new line. each letter is repeated for the length of the word"""
    
    for i in range(len(string)):
        print(string[i] * len(string))
    
vertical_strings('Pineapple')
vertical_strings('Hi')