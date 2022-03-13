# HOW TO PRINT DIGITAL CLOCK USING PYTHON
# First we install the font package from site
# import all libraries related to tkinter
# i have already installed tkinter
from tkinter import*  # Tkinter is a standard GUI library
from tkinter.ttk import * #Import all library of tkinter 
from time import strftime
root=Tk()    #Tk claas is used to create a root window 
root.title("Digital Clock")   #title() set the title of the window

def time():
    string=strftime('%H:%M:%S %p')    # declare the time format
    lable.config(text=string)
    lable.after(1000,time)    # delay time declaration 
lable=Label(root,font=("ds-digital",100),background="black",foreground="lime") 
lable.pack(anchor='center')
time()    #call the time function
mainloop()

#thanks for watching this video
#please like,share,subscribe my video

