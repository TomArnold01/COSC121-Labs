""" asks for input and then changes it to bee latin then prints goodbye in 
    bee latin aswell
    Written fo Test 2 
    Author: Tom Arnold 
    Date: 23/09/2021
"""
    
def get_string():
    """askes for inputs"""
    string = input("Enter English sentence: ")
    return(string)

def latinize_sentence(string):
    """ to convert words starting with a non_consonant"""
    vowel = 'a', 'e', 'i', 'o', 'u'
    number = '1', '2', '3', '4', '5', '6', '7', '8', '9'
    consonant = 'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'
    lower = string.lower()
    result = ''
    for i in lower.split():    
        if i.startswith(vowel): 
            new_word_vowel = i + 'buzz '
            result += new_word_vowel
       
        elif i.startswith(number):
            new_word_num = i + 'buzz '
            result += new_word_num            
       
        elif i.startswith(consonant):
            if i != number:
                new_word_non = i[1:] + i[0] + "uzz "
                result += new_word_non 
        else:
            new_word_vowel = i + 'buzz '
            result += new_word_vowel            
    new_word = result
    return new_word

def print_result(new_word, string):
    """prints the bee latin of string"""
    while string != 'q':
    
        print("Bee latin = {}".format(new_word))
        string = get_string()
    if string == 'q':
        print("oodbyeguzz")
    return string
        
def main():
    """The main function"""
    string = get_string()
    get_bee_latin = latinize_sentence(string)
    outcome = print_result(get_bee_latin, string)
    
main()