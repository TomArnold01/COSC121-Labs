def same_ends(string_1, string_2):
    if string_1[0] == string_2[0] and string_1[-1] == string_2[-1] and not string_1 ==string_2:
        return True
    elif string_1 == string_2:
        return False
    if string_1[0] == string_2[0] or string_1[-1] ==  string_2[-1]:
        return False
    
print(same_ends("thing","thing"))