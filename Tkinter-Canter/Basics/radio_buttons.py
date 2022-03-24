import tkinter
from tkinter import IntVar

# Define window
root = tkinter.Tk()
root.title('Radio Buttons Basics')
root.iconbitmap('thinking.ico')
root.geometry('500x500')
root.resizable(0,0)
root.config(bg = '#444')

# Define Functions
def make_label():
    '''Print to the screen'''
    if number.get() == 1:
        num_label = tkinter.Label(output_frame, text='1 one 1')
    elif number.get() == 2:
        num_label = tkinter.Label(output_frame, text='2 two 2')
    num_label.pack()

# Define Frames
input_frame = tkinter.LabelFrame(root, text='This is fun', width=500, height=150)
output_frame = tkinter.LabelFrame(root, width=500, height=350)

input_frame.pack(padx = 10, pady=10)
output_frame.pack(padx = 10, pady=(0,10))


# Define Radio Buttons
number = IntVar()
number.set(1)
# Define Widgets
radio_1 = tkinter.Radiobutton(input_frame, text='Print the number one!', variable=number, value=1)
radio_2 = tkinter.Radiobutton(input_frame, text='Print the number two!', variable=number, value=2)
print_button = tkinter.Button(input_frame, text='Print the number!', command=make_label)


radio_1.grid(row=0, column=0, padx=10, pady=(0,10))
radio_2.grid(row=0, column=1, padx=10, pady=(0,10))
print_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


# Keep output frame size 
output_frame.pack_propagate(0)


#Run root window's main loop
root.mainloop()