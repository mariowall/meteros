from tkinter import *

text = Tk()
text.title("MeterTXT")
frame = Frame(text).pack(side = TOP)
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
        file.close()
opens = Button(frame ,text='Open',command=openly,bg='yellow')
opens.pack(side = LEFT)
save = Button(frame,text='Save',command=save,bg='yellow')
save.pack(side = LEFT)
scrolly = Text(text, width=100, height=50)
scrolly.pack()


mainloop()
