from tkinter import *
from tkinter.ttk import *

def say_hello():
    """The event handler for clicks on the button"""
    global hello_label, click_count
    click_count += 1
    if click_count == 1:
        hello_label['text'] = "Hello World!"
    elif click_count == 2:
        hello_label['text'] = "Hello again!"
    else:
        hello_label['text'] = "Yeah, yeah. That's enough."

def main():
    """Set up the GUI and run it. """

    global hello_label, click_count

    click_count = 0  # Global button click counter
    window = Tk()
    hello_label = Label(window, text='Is anyone there?')
    hello_label.grid(row=0, column=0)
    hello_button = Button(window, text="Say hello", command=say_hello)
    hello_button.grid(row=1, column=0)
    window.mainloop()

main()