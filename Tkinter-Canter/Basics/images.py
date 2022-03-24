import tkinter
from PIL import ImageTk, Image

#Define window
root = tkinter.Tk()
root.title('Images Basics')
root.iconbitmap('thinking.ico')
root.geometry('500x500')
root.resizable(0,0)
root.config(bg = '#4578a9')

# Basics... works for png
my_image = tkinter.PhotoImage(file='shield.png')
my_label = tkinter.Label(root, image=my_image)
my_label.pack()

my_button = tkinter.Button(root, image=my_image)
my_button.pack()

# Using PIL for JPEG
wavy_image = ImageTk.PhotoImage(Image.open('paint-masterpiece.jpeg'))
wavy_label = tkinter.Label(root, image=wavy_image)
wavy_label.pack()

#Run root window's main loop
root.mainloop()