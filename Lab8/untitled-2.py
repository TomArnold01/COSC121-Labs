def latinize_sentence(str):
    """ this will just latinize a word to start of with"""
    for i in str.split():
        print(i[0])
        if i[0] == ('a' and 'e' and 'i' and 'o' and 'u'):
            print("test")
       #     print(i[0].lower())
        #    print("ur smart")
        #    print(i)



bee_latin = latinize_sentence("The quick  red   oox")
print(bee_latin)
