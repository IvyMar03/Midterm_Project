from tkinter import *

# create workspace
ws = Tk()
ws.title("First Program")
ws.geometry('250x150')
ws.configure(bg="#567")

# function
def welcome():
    name = nameTf.get()
    Label(ws, text=f'Welcome {name}', pady=15, bg='#567').grid(row=2, columnspan=2)

# widgets
nameLb = Label(ws, text="Enter Your Name", pady=15, padx=10, bg='#567')
nameTf = Entry(ws)
welBtn = Button(ws, text="ClickMe!", command=welcome)

# positioning
nameLb.grid(row=0, column=0)
nameTf.grid(row=0, column=1)
welBtn.grid(row=1, columnspan=2)

# keep window open
ws.mainloop()
