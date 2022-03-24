#Window Basics
import tkinter

#Define window
root = tkinter.Tk()
root.title('Window Basics')
root.iconbitmap('thinking.ico')
root.geometry('250x500')
root.resizable(1,0)
root.config(bg='#ad75a8')

#Second window
top = tkinter.Toplevel()
top.title('Second Window')
top.config(bg='#405598')
top.geometry('200x200+500+50')

#Run root window's main loop
root.mainloop()