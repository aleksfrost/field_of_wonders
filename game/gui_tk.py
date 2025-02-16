from tkinter import *

def finish():
    root.destroy()
    print("Windows closed by user")

root = Tk()
root.title("The field of wonders")
root.geometry("500x500")

label = Label(text="Hello METANIT.COM")
label.pack()
root.protocol("WM_DELETE_WINDOW", finish)

root.mainloop()