class Zoogle:
    """Defines the Zoogle class
    Data attributes: role as type str 
                     name as type str 
                     health as tpye float
    """
    def __init__(self, role, name, health):
        """Creates the Zoogle object"""
        if role not in ['Grubling', 'Throve', 'Plaguelet']:
            raise ValueError('Invalid Zoogle role')
        if health <= 0:
            health = 0 
        self.role = role
        self.name = name
        self.health = health
        
    def __str__(self):
        """Returns string rep of the Zoogle details"""
        template = "{1} ({0}), health = {2:3.1f}"
        return template.format(self.role, self.name, self.health)
        
    def pain(self, health_lost):
        """Takes a value of the amount of the health that is lost due to pain
        0 is the lowest health that a Zoogle have"""
        total = self.health - health_lost
        if total <= 0:
            self.health = 0
            return self.health
        else:    
            self.health = total
            return self.health
    
    def drink_health_potion(self, health_gained):
        """Takes a value of the amount of the health that is gain due to magic
           """
        self.health = self.health + health_gained
        return self.health
