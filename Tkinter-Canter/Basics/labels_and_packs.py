import tkinter
from tkinter import BOTH

#Define window
root = tkinter.Tk()
root.title('Label Basics')
root.iconbitmap('thinking.ico')
root.geometry('500x500')
root.resizable(0,0)
root.config(bg = '#4578a9')

#Create Widgets
name_label_1 = tkinter.Label(root, text='Hello My Name is Arkadeep')
name_label_1.pack()

name_label_2 = tkinter.Label(root, text='Hello My Name is Blighter', font=('Arial', 10))
name_label_2.pack()

name_label_3 = tkinter.Label(root)
name_label_3.config(text = "Hello, My name is Paul Muad'dib")
name_label_3.config(font=('Cambria', 18, 'bold'))
name_label_3.config(bg = '#ea89ae')
name_label_3.pack(padx = 10, pady=50)

name_label_4 = tkinter.Label(root, text="Soo Soo Suuk!", fg = '#f2ea56', bg ='#011',font=('Arial', 12))
name_label_4.pack(pady = (0,10), ipadx = 10, ipady = 30, anchor='w')

name_label_5 = tkinter.Label(root, text="Muad'dib! Muad'dib! Muad'dib!", fg = '#12ea56', bg ='#333',font=('Arial', 18))
name_label_5.pack(pady = (0,10), ipadx = 20, ipady = 10, fill=BOTH, expand = True)

#Run root window's main loop
root.mainloop()