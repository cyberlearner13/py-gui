#Buttons and Grid
import tkinter

#Define window
root = tkinter.Tk()
root.title('Buttons_Grids Basics')
root.iconbitmap('thinking.ico')
root.geometry('500x500')
root.resizable(0,0)
root.config(bg = '#4578a9')

#Define layout
name_button = tkinter.Button(root, text="Name")
name_button.grid(row=1, column=2)

time_button = tkinter.Button(root, text="Time", bg = '#a897d9')
time_button.grid(row=0, column=1)

place_button = tkinter.Button(root, text="Place", bg="#784589", activebackground="#99ff93")
place_button.grid(row=2, column=4, padx=10, pady=20, ipadx=15)

day_button = tkinter.Button(root, text="Day", bg="black", fg="white", borderwidth=5)
day_button.grid(row=5, column=0, columnspan=3, sticky='WE')


test_1 = tkinter.Button(root, text="TEST")
test_2 = tkinter.Button(root, text="TEST")
test_3 = tkinter.Button(root, text="TEST")
test_4 = tkinter.Button(root, text="TEST")
test_5 = tkinter.Button(root, text="TEST")
test_6 = tkinter.Button(root, text="TEST")

test_1.grid(row=2, column=0, padx=5, pady=5)
test_2.grid(row=2, column=1, padx=5, pady=5)
test_3.grid(row=2, column=2, padx=5, pady=5)
test_4.grid(row=3, column=0, padx=5, pady=5)
test_5.grid(row=3, column=1, padx=5, pady=5)
test_6.grid(row=3, column=2, padx=5, pady=5)

#Run root window's main loop
root.mainloop()