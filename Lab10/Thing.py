class Thing:
    """Defines the Thing class
    Data attributes: name as type str
                     heigth as type float 
                     words as tpye list
    """
    def __init__(self, name, height, words):
        """Creates the Thing objects"""
        
        self.name = name
        self.height = height
        self.words = words 
    
    def taller_by(self, value):
        """ add the value to the persons height"""
        self.height += value
        
    def learn(self, value):
        """Adds a new word that has been learnt"""
        self.words += value
    
    def __str__(self):
        """Returns a string"""
        template = ""
        template += "Hi. I'm {0}. I'm {1} cm tall.\n".format(self.name, self.height)
        template += "Words I know: "
        
        for i in range(len(self.words)):
            if i != len(self.words) -1:
                template += self.words[i] + ", "
            else:
                template += self.words[i] +"."
        return template
    