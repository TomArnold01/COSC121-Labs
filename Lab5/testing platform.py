def file_size(filename):
    """ returns a count of the number of characters in the file"""
    filename = open('data.txt', "r")
    count = 0
    for letter in infile.read():
        count += 1
    return count 

	
print(file_size('data.txt'))