import re
import tkinter as tk
from tkinter import ttk
from tkinter import *
root = tk.Tk()
root.title("DNA Palindromes")
#root.geometry("800x600")
root['bg'] = '#aed6f1'
frame_1 = tk.Frame(root, width=400, height=500, bg='#aed6f1')

frame_1.pack(side = 'left')
frame_2 = tk.Frame(root, height=500, bg =  '#d6eaf8')
frame_2.pack(side='right')

#root.geometry("1000x500")
#dna_file = open("Test.txt", "r")
#content = dna_file.read()
#content = content.replace(' ', '')
#content = content.upper()



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
    while len(working_content) >= min_len*2:       
        regex = re.search(current_comp_reverse, working_content)
        if regex != None:            
            palindromes += 1            
            palindrome_start_index = regex.span()[0] + removed_char + 1
            palindrome_end_index = regex.span()[1] + removed_char  
            print(f"From {current_start_index} to {current_end_index} ({comp(reverse_comp(current_comp_reverse))})")
            print(f"Found in {palindrome_start_index} to {palindrome_end_index} ({current_comp_reverse})")
            print('- - - - - - - - - - - - - - -')
            working_content = skip_all(working_content, regex.span()[1])
            removed_char += regex.span()[1]
            

            lab = tk.Label(frame_2,text=f"From {current_start_index} to {current_end_index} ({comp(reverse_comp(current_comp_reverse))})", bg =  '#d6eaf8')
            lab2 = tk.Label(frame_2, text = f"Found in {palindrome_start_index} to {palindrome_end_index} ({current_comp_reverse})",bg =  '#d6eaf8')
            lab3 = tk.Label(frame_2, text = '- - - - - - - - - - - - - - -', bg =  '#d6eaf8')
            lab.pack()
            lab2.pack()
            lab3.pack()
            
            
        else:
            break
    return palindromes

def restart():
    root.destroy()
    run()
    
def run():
    palindromes = 0
    current_start_index = 0
    content = entry1.get()
    content = content.replace(' ', '')
    content = content.upper()
    min_len = (entry2.get())
    min_len = int(min_len)
    
    initial_content = (content)
    
    lab00 = tk.Label(frame_2,text= "Original sequence is: ", bg =  '#d6eaf8')
    lab0 = tk.Label(frame_2,text=initial_content, bg =  '#d6eaf8')
    lab01 = tk.Label(frame_2,text='- - - - - - - - - - - - - - - ', bg =  '#d6eaf8')
    lab02 = tk.Label(frame_2,text= f"Palindromes of length {min_len} are: ", bg =  '#d6eaf8')
    lab00.config(font=('helvetica', 16))
    lab02.config(font=('helvetica', 16))    
    lab00.pack()
    lab0.pack()
    lab01.pack()
    lab02.pack()

    while len(content) >= min_len*2:
        current = content[:min_len]
        current_comp = comp(current)
        current_comp_reverse = reverse_comp(current_comp)
        working_content = remove_current(content, min_len)
        palindromes += look_for_matches(current_comp_reverse, working_content, current_start_index, min_len)
        content = skip_first(content)
        current_start_index += 1

    print('Finished')
    print('There are ' + str(palindromes) + ' palindromes')
    lab4 = tk.Label(frame_2, text = 'There are ' + str(palindromes) + ' palindromes')
    lab4.config(font=('helvetica', 16), bg= '#d6eaf8')
    lab4.pack()  


# imagen = tk.PhotoImage(file="tec.gif")
# tk.Label(root, image=imagen, bd=0).pack()

#entry1_var = tk.StringVar()
entry1 = ttk.Entry(frame_1, background= '#aed6f1')
#entry1.pack()

#entry2_var = tk.StringVar()
entry2 = ttk.Entry(frame_1, background= '#aed6f1')
#entry2.pack()

#entry1.insert(0, "Insert here a DNA Sequence")
label_seq = tk.Label(frame_1, text = "Insert here a DNA Sequence:")
label_seq.config(font=('helvetica', 16), bg= '#aed6f1')
label_seq.place(x=95, y=50)
entry1.place(x=100, y=100)

label_len = tk.Label(frame_1, text = "Insert here the minimum length of palindrome:")
label_len.config(font=('helvetica', 16), bg= '#aed6f1')
label_len.place(x=50, y=150)
entry2.insert(0, 0)
entry2.place(x=100, y=200)
button = ttk.Button(frame_1, text="Obtain Palindromes", command=run)
button.place(x=110, y=250)
button = ttk.Button(frame_1, text="Restart", command=restart)
button.place(x=110, y=400)
root.mainloop()


