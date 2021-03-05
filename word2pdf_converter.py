import tkinter as tk
from docx2pdf import convert
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Word to PDF")
root.geometry("300x50")
root.configure(bg="lightgrey")

def word2pdf():
    file = askopenfile(filetype = [('word file', '*.docs')])
    convert(file.name)
    showinfo("Done","File Successfully Converted ")


lable = tk.Label(root,text='Choose Files: ')
lable.grid(row=0, column=0, padx=5, pady=5)

button = ttk.Button(root,text = "Convert WordToPdf", width=30, command=word2pdf)
button.grid(row=0, column=1, padx=5, pady=5)

root.mainloop()
