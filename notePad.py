from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('NOTE PAD')
root.geometry('500x500')
root.resizable(False,False)


#functions
def new_file():
    text_box.delete(1.0,END)



def open_file():
    file=filedialog.askopenfile(mode='r',filetypes=[('text file','*.txt')])
    if file is not None:
        content=file.read()

    text_box.insert(INSERT,content)



def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    txt=str(text_box.get(1.0,END))
    open_file.write(txt)
    open_file.close()




#menu

menubar=Menu(root)
root.config(menu=menubar,bg='gray')

#menu-file

file_menu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label='New',command=new_file)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label='Save',command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.destroy)
#menu-help
help_menu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=help_menu)
help_menu.add_command(label='welcome')
help_menu.add_command(label='About')

#TextBox

text_box=Text(root,height='38',width='71',wrap=WORD)
text_box.place(x=0,y=0)


root.mainloop()
