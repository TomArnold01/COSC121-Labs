def read_data(filename):
    """Read and return the contents of the given file.
       The file is assumed to exist, or an exception will occur.
       It is also assumed that each line of the file consists of a
       student name, a comma, and a floating-point mark.
       Returns: a list of (name, mark) tuples, where name is a string
       and mark is a floating-point number.
    """
    try:
        file = open(filename,"r") 
        lines = file.read().strip().split("\n")
        
        content = []
        test = []
        for i in lines:
            mark = float(i[-2:])
            name = i[:-3]
            content.append(tuple(name.split()))
            test.append(mark)
            outcome =  content + test
            print(outcome)
       
       
       
       
        return content
    except FileNotFoundError:
        print("File not found to read")

        
        
data = read_data('data.csv')
for item in data:
    print(item)