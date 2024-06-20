from tkinter import *
from tkinter.ttk import *

TEMPLATE = "Name: {0}\nHeight: {1:.2f} m\nHorns: {2}"

class Blork(object):
    """Defines the Blork class.
    Note that we've declared this explicitly as a subclass of object.
    Data attributes: name of type str
                     height (metres) of type float
                     has_horns of type bool    
    """

    def __init__(self, name, height, has_horns=False):
        """Blork constructor"""
        self.name = name
        self.height = height
        self.has_horns = has_horns
        

class BlorkGui(object):
    """Defines the Blork Interface
       Note that we've declared this explicitly as a subclass of object.
    """
    
    def __init__(self, window, blorks):
        """Setup the label and button on given window"""
        #combo box
        self.blorks = blorks
        self.name_options = []
        for i in blorks.keys():
            self.name_options.append(i)
        
        self.name_combo = Combobox(window,
                                 values=self.name_options)
        self.name_combo.grid(row=0, column=0) 
        self.name_combo.current(0)
        
        #Button
        self.action_button = Button(window,
                                   text="View details", command=self.select)
        self.action_button.grid(row=0, column=1)
        
        #label thing
        self.detail_label = Label(window, 
                                  text ="Press 'View details'")
        self.detail_label.grid(row=1, column=0) 

    def select(self):
        """Changes the details"""
        value = self.name_combo.get()
        name = self.blorks.get(value).name
        height = self.blorks.get(value).height
        has_horns = self.blorks.get(value).has_horns
        horns = "No"
        if has_horns:
            horns = "Yes"
            
        self.detail_label['text'] = "Name: " + name + "\nHeight :" + str(
            float("{:.2f}".format(height))) + ' \nHorns: ' + horns
        

def main():
    """Set up the GUI and run it."""    
    blork_dict = {"Jeff": Blork("Jeff", 1.6),
              "Lily": Blork("Lily", 1.111111),
              "Jack": Blork("Jack", 1.89),
              "Chewblorka": Blork("Chewblorka", 3.14, True),
              "Blorkstien": Blork("Blorkstien", 0.856, True)}
    
    window = Tk()
    blork_gui = BlorkGui(window, blork_dict)
    window.mainloop()

main()
