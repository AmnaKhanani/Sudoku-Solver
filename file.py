from tkinter import *
window=Tk()
window.geometry('350x200')
window.title('File Handling')
file_entry=Entry(window,width=10)
lbl=Label(window,text='File name:')
lbl.pack()
file_entry.pack()
def read():
    try:
        infile=open(file_entry.get())
        lbl=Label(window,text=infile.read())
        lbl.pack()
        infile.close()
    except FileNotFoundError as err:
        print(err)
        
btn=Button(window,text='read file',command=read)
btn.pack()
window.mainloop()
