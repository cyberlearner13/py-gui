import tkinter
from tkinter import RIGHT, END, DISABLED, NORMAL

#Define window
root = tkinter.Tk()
root.title('Calculator')
root.iconbitmap('calc.ico')
root.geometry('400x400')
root.resizable(0,0)

#Define colors and fonts
dark_green = '#93af22'
light_green = '#acc253'
white_green = '#edefe0'
button_font = ('Arial', 18)
display_font = ('Arial', 30)

#GUI Layout
#Define frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root)
display_frame.pack(padx=2, pady=(5,20))
button_frame.pack(padx=2, pady=5)

#Layout for the display frame
display = tkinter.Entry(display_frame, width=50, font=display_font, bg=white_green,
borderwidth=5, justify=RIGHT)
display.pack(padx=5, pady=5)

#Layout for the button frame
clear_button = tkinter.Button(button_frame, text="Clear", font=button_font, bg=dark_green)
quit_button = tkinter.Button(button_frame, text="Quit", font=button_font, bg=dark_green, command=root.destroy)

inverse_button = tkinter.Button(button_frame, text='1/x', font=button_font, bg=light_green)
square_button = tkinter.Button(button_frame, text='x^2', font=button_font, bg=light_green)
exponent_button = tkinter.Button(button_frame, text='x^n', font=button_font, bg=light_green)
divide_button = tkinter.Button(button_frame, text=' / ', font=button_font, bg=light_green)

multiply_button = tkinter.Button(button_frame, text='*', font=button_font, bg=light_green)
subtract_button = tkinter.Button(button_frame, text='-', font=button_font, bg=light_green)
add_button = tkinter.Button(button_frame, text='+', font=button_font, bg=light_green)
equal_button = tkinter.Button(button_frame, text='=', font=button_font, bg=dark_green)

decimal_button = tkinter.Button(button_frame, text='.', font=button_font, bg='black', fg='white')
negate_button = tkinter.Button(button_frame, text='+/-', font=button_font, bg='black', fg='white') 

nine_button = tkinter.Button(button_frame, text='9', font=button_font, bg='black', fg='white')
eight_button = tkinter.Button(button_frame, text='8', font=button_font, bg='black', fg='white')
seven_button = tkinter.Button(button_frame, text='7', font=button_font, bg='black', fg='white')
six_button = tkinter.Button(button_frame, text='6', font=button_font, bg='black', fg='white')
five_button = tkinter.Button(button_frame, text='5', font=button_font, bg='black', fg='white')
four_button = tkinter.Button(button_frame, text='4', font=button_font, bg='black', fg='white')
three_button = tkinter.Button(button_frame, text='3', font=button_font, bg='black', fg='white')
two_button = tkinter.Button(button_frame, text='2', font=button_font, bg='black', fg='white')
one_button = tkinter.Button(button_frame, text='1', font=button_font, bg='black', fg='white')
zero_button = tkinter.Button(button_frame, text='0', font=button_font, bg='black', fg='white') 


#First row
clear_button.grid(row=0, column=0, columnspan=2, pady=1, sticky="WE")
quit_button.grid(row=0, column=2, columnspan=2, pady=1, sticky="WE")

#Second row
inverse_button.grid(row=1, column=0, pady=1, sticky="WE")
square_button.grid(row=1, column=1, pady=1, sticky="WE")
exponent_button.grid(row=1, column=2, pady=1, sticky="WE")
divide_button.grid(row=1, column=3, pady=1, sticky="WE")

#Third row (Add padding to create the size of the columns)
seven_button.grid(row=2, column=0, pady=1, sticky="WE", ipadx=20)
eight_button.grid(row=2, column=1, pady=1, sticky="WE", ipadx=20)
nine_button.grid(row=2, column=2, pady=1, sticky="WE", ipadx=20)
multiply_button.grid(row=2, column=3, pady=1, sticky="WE", ipadx=20)

#Fourth row
four_button.grid(row=3, column=0, pady=1, sticky="WE")
five_button.grid(row=3, column=1, pady=1, sticky="WE")
six_button.grid(row=3, column=2, pady=1, sticky="WE")
subtract_button.grid(row=3, column=3, pady=1, sticky="WE")

#Fifth row
one_button.grid(row=4, column=0, pady=1, sticky="WE")
two_button.grid(row=4, column=1, pady=1, sticky="WE")
three_button.grid(row=4, column=2, pady=1, sticky="WE")
add_button.grid(row=4, column=3, pady=1, sticky="WE")

#Sixth row
negate_button.grid(row=5, column=0, pady=1, sticky="WE")
zero_button.grid(row=5, column=1, pady=1, sticky="WE")
decimal_button.grid(row=5, column=2, pady=1, sticky="WE")
equal_button.grid(row=5, column=3, pady=1, sticky="WE")

#Run root window's main loop
root.mainloop()
