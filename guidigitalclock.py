'''Simple Tkinter GUI Digital Clock''' 

# importing required modules
from tkinter import *
import time

# time function
def times():
    
    current_time = time.strftime ("%I:%M:%S:%p")
    clock_lbl = Label(root , font="Times 11", bg="black",fg="red",text=current_time )
    clock_lbl.after(200, times)
    clock_lbl.place(x=60, y=60)

# main gui window
root=Tk()

root.title("Digital Clock")
root.geometry("500x300")
root.resizable(False,False)
root.configure(background="black")

# quit button widget
quitButton = Button(root, text="Close",font="Times 4",fg="red",bg="black",command=root.quit)
quitButton.place(x=170,y=190)
times()
    
root.mainloop()

'''Author Info''' 
'''
   Name: Eihctir A.K.A Rlyonheart
   Github| www.github.com/rlyonheart
   Twitter| www.twitter.com/rly0nheart
   Instagram| www.instagram.com/rlyonheart
'''
