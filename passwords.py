#import every function
import random
import string
from tkinter import *
#gui
root = Tk()
#username/email
entrywidget1 = Entry(root, width=50)
entrywidget1.insert(0, "Username/email: ")
entrywidget1.pack()
#website
entrywidget2 = Entry(root, width=50)
entrywidget2.insert(0, "Website: ")
entrywidget2.pack()
#def generator
def click():
    y = random.choice(string.ascii_letters)
    for i in range (0, 20):
        x = random.randint(0,2)
        if x == 0:
            y = y + random.choice(string.ascii_letters)
        if x == 1:
            y = y + random.choice(string.punctuation)
        if x == 0:
            y = y + random.choice(string.digits)
    #open and work on file
    my_file = open("password.txt", "a")
    my_file.write("\n" + "\n" + "email: " + entrywidget1.get() + "\n" + "site: " + entrywidget2.get() + "\n" "password: " + y)
    #label the result
    label = Label(root, text="\n" + "\n" + "email: " + entrywidget1.get() + "\n" + "site: " + entrywidget2.get() + "\n" "password: " + y)
    label.pack()
#button
myButton = Button(root, text="Create Password", command=click)
myButton.pack()
#make everything work
root.mainloop()