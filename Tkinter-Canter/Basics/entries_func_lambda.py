import tkinter
from tkinter import END

#Define window
root = tkinter.Tk()
root.title('Entries_Functions_Lambdas Basics')
root.iconbitmap('thinking.ico')
root.geometry('500x500')
root.resizable(0,0)
root.config(bg = '#444')

# Define functions

def make_label():
    '''Print a label to the app'''
    text = tkinter.Label(output_frame, text=text_entry.get(), bg='#f7647c')
    text.pack()

    text_entry.delete(0, END)


def count_up(number):
    '''Count up on the app'''
    global value
    text = tkinter.Label(output_frame, text=number,bg='#f7647c')
    text.pack()

    value = number + 1

# Define Frames
input_frame = tkinter.Frame(root, bg='#4879fc', width=500, height=100)
output_frame = tkinter.Frame(root, bg='#f7647c', width=500, height=400)

input_frame.pack(padx = 10, pady=10)
output_frame.pack(padx = 10, pady=(0,10))

# add entry
text_entry = tkinter.Entry(input_frame,width=40)
text_entry.grid(row=0, column=0, padx=5, pady=5)
input_frame.grid_propagate(0)

print_button = tkinter.Button(input_frame, text='Print!', command=make_label)
print_button.grid(row=0, column=1, padx=5, pady=5, ipadx=30)

# Keep output frame size 
output_frame.pack_propagate(0)

# Pass a parameter
value = 0
count_button = tkinter.Button(input_frame, text='Count!', command=lambda:count_up(value))
count_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='WE')
#Run root window's main loop
root.mainloop()