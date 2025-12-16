from tkinter import *

w = Tk()
w.title("Otter")

photo = PhotoImage(file="./assets/Otter.png")
photo1 = PhotoImage(file="./assets/otter_Logo.png")
w.iconphoto(True, photo)

#this creates a label widget
lable = Label(w, 
              text="Hello World", #text to display
              font=("Arial", 24, ''), #the font type and size 
              fg="Green", #text color
              bg="black", #background color around the text
              relief=RAISED, #makes a border around the label
              bd=10, #border width
              padx=0, #horizontal padding
              pady=0, #vertical padding
              image=photo1, #image to display
              compound='bottom', #position of the image relative to the text
              )

lable.pack() # places the label in the window
#lable.place(x=0, y=0)

w.mainloop()