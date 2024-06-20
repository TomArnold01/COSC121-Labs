def same_ends(string_1, string_2):
    """ takes two non-empty strings and returns True if string_1 and string_2 
    both start and end with the same character, except if string_1 is equal to
    string_2"""
    string_1[-1] = '1_-1'
    string_1[0] = '1_0'
    string_2[-1] = '2_-1'
    string_2[0] = '2_0'
    
    if '1_-1' == '2_-1' and '1_0' == '2_0' and string_1 != string_2:
            return True
        
    else:
        return False