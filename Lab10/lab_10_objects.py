"""File for creating Person objects"""

class Person:
    """Defines a Person class, suitable for use in a hospital context.
    Data attributes: name of type str
                     age of type int
                     weight (kg) of type float
                     height (metres) of type float
    Methods: bmi()
    """
    def __init__(self, name, age, weight, height):
        """Creates a new Person object with the specified name, age, weight
           and height"""
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def bmi(self):
        """Returns the body mass index of the person"""
        return self.weight / (self.height * self.height)
    
    def status(self):
        """ Returns the status of of a persons bmi"""
        bmi = self.bmi()
        if bmi < 18.5:
            return "Underweight"
        if bmi >= 18.5 and bmi < 25:
            return "Normal"
        if bmi >= 25 and bmi < 30:
            return "Overweight"
        if bmi >= 30:
            return "Obese"
        
        
    def __str__(self):
        """Returns the formatted string representation of the Person object"""
        template = "{0} ({1}) has a bmi of {2:3.2f}. Their status is {3}."
        return template.format(self.name, self.age, self.bmi(), self.status())

def read_people(csv_filename):
    """Opens and reads the data in the file"""
    ans = []
    with open(csv_filename) as file:
        lines = file.readlines()
        for line in lines:
            name, age, weight, height = line.split(",")
            age = int(age)
            weight = float(weight)
            height = float(height)
            a_person = Person(name, age, weight, height)
            ans.append(a_person)
    return ans 

def filter_people(people, status_string):
    """Filters the list it groups ofbmi statuses"""
    person = []
    for each in people:
        if each.status() == status_string:
            person.append(each)
            
    return person

  
def age_value(person):
    """To pick the age so it can be sorted"""
    return person.age


def bmi_value(person):
    """To pick out the bmi value so it can be sorted"""
    return person.bmi()
