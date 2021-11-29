import re
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext
from tkinter.font import BOLD
from PIL import ImageTk, Image
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os.path


root = tk.Tk()
root.title("DNA Palindromes")
#root.geometry("800x600")
root['bg'] = '#aed6f1'
frame_title = tk.Frame(root, bg = '#3279ff', height= 100)
frame_title.pack(side = 'top', fill= X)
label_title = tk.Label(frame_title, text = 'DNApp', bg = '#3279ff')
label_title.config(font=('helvetica', 24), fg = 'white')
label_title.pack(side = 'left', anchor = 'center')

tec_logo= Image.open("tec.png")
tec_logo = tec_logo.resize((200,80))
render_2 = ImageTk.PhotoImage(tec_logo)
img_2 = Label(frame_title, image=render_2, bg = '#3279ff') 
img_2.pack(side = 'right')


frame_bottom = tk.Frame(root, bg = '#3279ff', height= 100)
frame_bottom.pack(side = 'bottom', fill= X)
label_bottom = tk.Label(frame_bottom, text = 'By: Guillermo Perez and Pablo Quihui', bg = '#3279ff', fg = 'white', font=('helvetica', 16))
label_bottom.pack(anchor = 'e')
frame_1 = tk.Frame(root, width=500, height=600, bg='#aed6f1')
frame_1.pack(side = 'left')


class VerticalScrolledFrame:
    """
    A vertically scrolled Frame that can be treated like any other Frame
    ie it needs a master and layout and it can be a master.
    :width:, :height:, :bg: are passed to the underlying Canvas
    :bg: and all other keyword arguments are passed to the inner Frame
    note that a widget layed out in this frame will have a self.master 3 layers deep,
    (outer Frame, Canvas, inner Frame) so 
    if you subclass this there is no built in way for the children to access it.
    You need to provide the controller separately.
    """
    def __init__(self, master, **kwargs):
        width = kwargs.pop('width', None)
        height = kwargs.pop('height', None)
        bg = kwargs.pop('bg', kwargs.pop('background', None))
        self.outer = tk.Frame(master, **kwargs)

        self.vsb = tk.Scrollbar(self.outer, orient=tk.VERTICAL)
        self.vsb.pack(fill=tk.Y, side=tk.RIGHT)
        self.canvas = tk.Canvas(self.outer, highlightthickness=0, width=width, height=height, bg=bg)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas['yscrollcommand'] = self.vsb.set
        # mouse scroll does not seem to work with just "bind"; You have
        # to use "bind_all". Therefore to use multiple windows you have
        # to bind_all in the current widget
        self.canvas.bind("<Enter>", self._bind_mouse)
        self.canvas.bind("<Leave>", self._unbind_mouse)
        self.vsb['command'] = self.canvas.yview

        self.inner = tk.Frame(self.canvas, bg=bg)
        # pack the inner Frame into the Canvas with the topleft corner 4 pixels offset
        self.canvas.create_window(4, 4, window=self.inner, anchor='nw')
        self.inner.bind("<Configure>", self._on_frame_configure)

        self.outer_attr = set(dir(tk.Widget))

    def __getattr__(self, item):
        if item in self.outer_attr:
            # geometry attributes etc (eg pack, destroy, tkraise) are passed on to self.outer
            return getattr(self.outer, item)
        else:
            # all other attributes (_w, children, etc) are passed to self.inner
            return getattr(self.inner, item)

    def _on_frame_configure(self, event=None):
        x1, y1, x2, y2 = self.canvas.bbox("all")
        height = self.canvas.winfo_height()
        self.canvas.config(scrollregion = (0,0, x2, max(y2, height)))

    def _bind_mouse(self, event=None):
        self.canvas.bind_all("<4>", self._on_mousewheel)
        self.canvas.bind_all("<5>", self._on_mousewheel)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mouse(self, event=None):
        self.canvas.unbind_all("<4>")
        self.canvas.unbind_all("<5>")
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        """Linux uses event.num; Windows / Mac uses event.delta"""
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units" )
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units" )

    def __str__(self):
        return str(self.outer)

frame_2 = VerticalScrolledFrame(root, height=500, bg='white')



def comp(current):
    current_comp = list(current)
    for k in range(0, len(current_comp)):
        if current_comp[k] == "A":
            current_comp[k] = "T"
        elif current_comp[k] == "G":
            current_comp[k] = "C"
        elif current_comp[k] == "T":
            current_comp[k] = "A"
        elif current_comp[k] == "C":
            current_comp[k] = "G"
    return "".join(current_comp)

def reverse_comp(current_comp):
    return current_comp[::-1]

def remove_current(content, min_len):
    return content[min_len:]

def skip_first(working_content):
    return working_content[1:]

def skip_all(working_content, palindrome_end_index):
    return working_content[palindrome_end_index:] #modificar variable de nombre
    

def look_for_matches(current_comp_reverse, working_content, current_start_index, min_len):
    palindromes = 0
    current_end_index = current_start_index + min_len - 1
    removed_char = current_end_index
    while len(working_content) >= min_len:       
        regex = re.search(current_comp_reverse, working_content)
        if regex != None:            
            palindromes += 1            
            palindrome_start_index = regex.span()[0] + removed_char + 1
            palindrome_end_index = regex.span()[1] + removed_char  
            #print(f"From {current_start_index} to {current_end_index} ({comp(reverse_comp(current_comp_reverse))})")
            #print(f"Found in {palindrome_start_index} to {palindrome_end_index} ({current_comp_reverse})")
            #print('- - - - - - - - - - - - - - -')
            working_content = skip_all(working_content, regex.span()[1])
            removed_char += regex.span()[1]
            
            if checkbox_value.get()  == True:
                file = open(path_name, "a")
                #file.write(f"From {current_start_index} to {current_end_index} ({comp(reverse_comp(current_comp_reverse))})\n")
                #file.write(f"Found in {palindrome_start_index} to {palindrome_end_index} ({current_comp_reverse})\n")
                #file.write('- - - - - - - - - - - - - - -\n')
                file.write(comp(reverse_comp(current_comp_reverse)))
                file.write(" " + current_comp_reverse)
                file.write("\n")
                file.close()
            lab = tk.Label(frame_2,text=f"From {current_start_index} to {current_end_index} ({comp(reverse_comp(current_comp_reverse))})", bg =  'white')
            lab2 = tk.Label(frame_2, text = f"Found in {palindrome_start_index} to {palindrome_end_index} ({current_comp_reverse})",bg =  'white')
            lab3 = tk.Label(frame_2, text = '- - - - - - - - - - - - - - -', bg =  'white')
            lab.pack()
            lab2.pack()
            lab3.pack()
            
            
        else:
            break
    return palindromes

    
def run():
    global path_name
    path_name = entry_path.get()
    path = 0
    if path_name == "":
        while os.path.isfile(f'output_{path}.txt'):
            path += 1
        path_name = f'output_{path}.txt'
    else: 
        path_name = f"{path_name}.txt"
    palindromes = 0
    current_start_index = 0
    content = text_input.get('1.0', tk.END)
    content = content.replace(' ', '')
    content = content.replace('\n', '')
    content = content.upper()
    min_len = (entry2.get())
    min_len = int(min_len)
    max_len = (entry3.get())
    max_len = int(max_len)
    initial_content = (content)
    frame_2.pack(side='right')
    lab02 = tk.Label(frame_2,text= f"Palindromes of length {min_len} are: ", bg =  'white')
    lab02.config(font=('helvetica', 16))    
    lab02.pack()

    for i in range(min_len, max_len + 1):
        content = initial_content
        while len(content) >= i:
            current = content[:i]
            current_comp = comp(current)
            current_comp_reverse = reverse_comp(current_comp)
            #print("comp reverse = " + current_comp_reverse)
            working_content = remove_current(content, i)
            #print("working content = " + working_content)
            palindromes += look_for_matches(current_comp_reverse, working_content, current_start_index, i)
            content = skip_first(content)
            current_start_index += 1

    print('Finished')
    print('There are ' + str(palindromes) + ' palindromes')
    lab4 = tk.Label(frame_2, text = 'There are ' + str(palindromes) + ' palindromes')
    lab4.config(font=('helvetica', 16), bg= 'white')
    lab4.pack()  


text_input = scrolledtext.ScrolledText(frame_1, width = 400, height = 150)
text_input.place(x=50, y=80, width=400, height=150)

entry2 = ttk.Entry(frame_1, background= '#aed6f1')
entry3 = ttk.Entry(frame_1, background= '#aed6f1')

label_seq = tk.Label(frame_1, text = "Insert here a DNA Sequence:")
label_seq.config(font=('helvetica', 16), bg= '#aed6f1')
label_seq.place(x=150, y=50)
checkbox_value = tk.BooleanVar()
checkbox = Checkbutton(frame_1, text="Save?", variable=checkbox_value, background= '#aed6f1')
#checkbox.config(background='#aed6f1')
checkbox.place(x=50, y=50)


label_len = tk.Label(frame_1, text = "Insert here the length of palindrome:")
label_len.config(font=('helvetica', 16), bg= '#aed6f1')
label_len.place(x=130, y=270)
label_min = tk.Label(frame_1, text = "Minimum:")
label_max = tk.Label(frame_1, text = "Maximum:")
label_min.config(font=('helvetica', 16), bg= '#aed6f1')
label_max.config(font=('helvetica', 16), bg= '#aed6f1')
label_min.place(x=60, y=300)
label_max.place(x=60, y=340)
entry2.insert(0, 0)
entry2.place(x=150, y=300, width = 200)

entry3.insert(0, 0)
entry3.place(x=150, y=340, width = 200)

button = ttk.Button(frame_1, text="Obtain Palindromes", command=run)
button.place(x=160, y=370, width=180)
button_close = ttk.Button(frame_1, text="Close", command=root.destroy)
button_close.place(x=10, y=560)

entry_path = ttk.Entry(frame_1, background= '#aed6f1')
entry_path.place(x = 350, y = 240, width = 100)
label_path = tk.Label(frame_1, text = "File Name Output:", bg= '#aed6f1')
label_path.place(x = 220, y = 240)

def open_text_file():
    # file type
    filetypes = (('text files', '*.txt'), ('all files', '*.*'))
    # show the open file dialog
    f = fd.askopenfilename(filetypes=filetypes)
    # read the text file and show its content on the Text
    text_input.insert('1.0', f.readlines())

# open file button
open_button = ttk.Button(frame_1, text='Open a Text File', command=open_text_file)
open_button.place(x=50, y=240)


#image dna

load= Image.open("DNA.png")
load = load.resize((300,200))
render = ImageTk.PhotoImage(load)
img = Label(frame_1, image=render, bg = '#aed6f1') 
img.place(x=100, y=400)

root.mainloop()


