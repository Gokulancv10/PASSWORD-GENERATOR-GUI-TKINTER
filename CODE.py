import random
try:
    import pyperclip
    from tkinter import *
    from tkinter.ttk import *
except ImportError:
    import Pyperclip
    from Tkinter import *
    from Tkinter.ttk import *

def low():
	entry.delete(0, END)

	length=var1.get()

	lower = 'abcdefghijklmnopqrstuvwxyz'
	upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	digits= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*_'
	password=''

	if var.get()==1:
		for i in range(0,length):
			password=password + random.choice(lower)
		return password

	elif var.get()==0:
		for i in range(0,length):
			password=password + random.choice(upper)
		return password

	elif var.get()==3:
		for i in range(0,length):
			password=password + random.choice(digits)
		return password

	else:
		print('Invalid value')


def generate():
	password1= low()
	entry.insert(10,password1)

def copy1():
	random_password = entry.get()
	pyperclip.copy(random_password)


root= Tk()
root.title('Random Password Generator')
root.geometry('450x50')


var= IntVar()
var1=IntVar()


password_label=Label(root,text='Password')
password_label.grid(row=0)
entry=Entry(root)
entry.grid(row=0,column=1)


password_length=Label(root,text='Length')
password_length.grid(row=1)


copy=Button(root,text='Copy',command=copy1)
copy.grid(row=0,column=2)


generate_button=Button(root,text='Generate',command=generate)
generate_button.grid(row=0,column=3)


radio_low=Radiobutton(root,text='Low',value=1,variable=var)
radio_low.grid(row=1,column=2,sticky='E')


radio_medium=Radiobutton(root,text='Medium',value=0,variable=var)
radio_medium.grid(row=1,column=3,sticky='E')

radio_strong=Radiobutton(root,text='Strong',value=3,variable=var)
radio_strong.grid(row=1,column=4,sticky='E')


Combobox=Combobox(root,textvariable=var1)
Combobox['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 
 				17, 18, 19, 20, 21, 22, 23, 24, 25, 
 				26, 27, 28, 29, 30, 31, 32)
Combobox.current(0)
Combobox.grid(row=1,column=1)

root.mainloop()
