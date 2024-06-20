""" This module asks for a filename reads it put the data into a list 
   that contains two tuples the first contains the course code and the 
   name of the course. and the second cotains the student number and the 
   first and last names of the student."""

def records_from_file(filename):
    """Returns a list of records from the given file. Each item in the list
       should be a tuple containing a course tuple and a student tuple.
    """
    infile = open(filename, "r")
    file = infile.read().strip().split('\n')[1:]
    infile.close()
    result = []
    
    for line in file:
        row_data = line.split(",")
        course = (row_data[0], row_data[1]) 
        student = (int(row_data[2]), row_data[3], row_data[4]) 
        result.append((course,student)) 
    return result  

def all_courses(records):
    """Returns a dictionary that maps course codes to the course names"""
    dict_course = {}
    for line in records:
        dict_course[line[0][0]] = line[0][1]
    return dict_course
    
def all_students(records):
    """Returns a dictonary that maps students numbers (as ints) to student 
       name tuples. ie the key is the student number and the value is the 
       studnet names
    """
    dict_number = {}
    for line in records:
        dict_number[line[1][0]] = line[1][1:]
    return dict_number

def course_rolls(records):
    """Returns a dictionary napping course codes to sets of student numbers
       ie the key will be the course code and the value will be sets of 
       student numbers
    """
    dict_code = {}
    for line in records:
        course, student = line
        key, _ = course
        value, *_ = student
        dict_code.setdefault(key, set())
        dict_code[key].add(value)
    return dict_code

def print_students(dictionary_student):
    """print the student number, student name, family name sorted by the 
       student number
    """
    print("All students:")
    for i in sorted (dictionary_student) :
        first_name = dictionary_student[i][0]
        last_name = dictionary_student[i][1]
        print(" ", str(i) + ":", first_name, last_name.upper())
    print()
    

def print_courses(dictionary_course):
    """Print the course code and course name sorted by course code
       """

    print("All courses:")
    for i in sorted (dictionary_course):
        print(" ", str(i) + ":", dictionary_course[i])
    print()

def print_rolls(dictionary_rolls): 
    """Prints the course code then a new line followed by the student number 
       and the student name
       """
    print("Course rolls:")
    print(dictionary_rolls)
  
    


def validate_command(command, argument, records, filename):
    """Confirms the command and if not good then displays and erroe message
       """
    
    if (command != "list"):
        print("Unknown command")
    else:
        if argument != "courses" and argument != "students" and argument != "rolls":
            print("Unknown argument for list command")
        elif argument == "courses":
            dictionary_course = all_courses(records)
            print_courses(dictionary_course) 
        elif argument == "students":
            dictionary_student = all_students(records) 
            print_students(dictionary_student) 
        elif argument == "rolls":
            dictionary_rolls = records_from_file(filename)
            print_rolls(dictionary_rolls)
            

def main():
    """Gets the filename and then responeds to commands
       """
    filename = input("Filename? ")
    
    records = records_from_file(filename)  # from line 6
    
    name = all_students(records) # from line 29
    
    command = ""
    while command != "quit":
        command_entered = input("Command: ")
        command_list = command_entered.split(" ")
        command = command_list[0]
        
        if (len(command_list) == 2):
            argument = command_list[1]
        else:
            argument = "";
        if command != "quit":
            validate_command(command, argument, records, filename)
        else:
            print("Adios")


main()