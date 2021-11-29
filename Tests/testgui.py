import tkinter as tk
from tkinter import ttk
root = tk.Tk()
frame = tk.Frame(root, width=500, height=500)
frame.pack()
frame.config(side = 'left')
def sequence():
    content = entry.get()
    print(content)
    return content


entre_var = tk.StringVar()
entry = ttk.Entry(root)
entry.pack()

button = ttk.Button(root, text='Click Me', command=sequence)
button.place(x=50, y=100)
#create input box tkinter
print(entry.get())

root.mainloop()
