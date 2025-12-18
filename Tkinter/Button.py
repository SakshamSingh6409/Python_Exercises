from tkinter import *
w = Tk()
w.title("Otter")
button = Button(w,
                text="Click Me", #text to display on the button
                command=lambda: print("Button Clicked!"), #function to call when button is clicked
                font=("Comic Sans MS", 30), #font type and size
                fg="Green", #text color
                bg="Black", #button background color
                activeforeground="Green", #text color when button is clicked
                activebackground="Black", #button background color when clicked
                relief=RAISED, #border style
)
button.pack() # places the button in the window
w.mainloop()