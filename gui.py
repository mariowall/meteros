from Tkinter import *

text = Tk()
text.title("MeterTXT")
frame = Frame(text).pack(side = TOP)
menubar = Menu(text)
def openly():
  files = filedialog.askopenfile(parent=text,mode='rb',title="Open")
  if files != None:
    omg = files.read()
    scrolly.insert("1.0",omg)
    omg.close()
def save():
    file = filedialog.asksaveasfile(mode='w')
    if file != None:
        data = scrolly.get('1.0', END+'-1c')
        file.write(data)
def about():
 about = Tk()
 about.title("About")
 al = Label(text="meterOS (c) copyright meteros inc made by\
 Prajwal Saokar and Sowmiyan NV.").pack()
 mainloop()

filemenu = Menu(menubar)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Open", command=openly)
menubar.add_cascade(label="File", menu=filemenu)

about = Menu(menubar)
about.add_command(label="About", command=about)
menubar.add_cascade(label='About', menu=about)

scrolly = Text(text, width=100, height=50)
scrolly.pack()

text.config(menu=menubar)
mainloop()
