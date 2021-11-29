import tkinter as tk
import subprocess

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 500,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Palindromes in DNA sequences')
label1.config(font=('helvetica', 16))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type a DNA sequence:')
label2.config(font=('helvetica', 12))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

label3 = tk.Label(root, text='Type a palindrome length:')
label3.config(font=('helvetica', 12))
canvas1.create_window(200, 190, window=label3)

entry2 = tk.Entry (root) 
canvas1.create_window(200, 230, window=entry2)

content = entry1.get()
min_len = (entry2.get())

def getPalindromes (content,min_len):
    #content = ''
    
    min_len = (min_len)

    
    # capture = io.StringIO()
    # save,sys.stdout = sys.stdout,capture
    
    #cmd = 'python DNApp3.py'
    #p = subprocess.Popen(cmd, shell = True)
    #out, err = p.communicate()
    # sys.stdout = save
    # x = capture.getvalue()
   
    
    label3 = tk.Label(root, text= 'The DNA palindromes of ' + content + ' is:',font=('helvetica', 10))
    canvas1.create_window(200, 300, window=label3)
    
    label4 = tk.Label(root, text= 'x',font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 350, window=label4)
    
    return content, min_len
    
button1 = tk.Button(text='Get the palindromes', command=getPalindromes(content,min_len), bg='brown', fg='black', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 270, window=button1)
    

root.mainloop()








