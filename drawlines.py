from tkinter import *

dritare = Tk()
dritare.geometry('800x600')
dritare.title('Draw Lines')

'''

forma = Canvas(dritare, bg = 'blue', width = 300, height = 300, bd = 10, relief = 'solid')
forma.pack()
# Line = x(fillimi),y(fillimi), x(mbarimi),y(mbarimi)
line = forma.create_line(0,0,400,400, fill = 'red', width = 10)
katror = forma.create_rectangle(20,20,180,80, fill = 'yellow', width = 10)
trekendshi = forma.create_polygon(100,10,10,150,200,150, fill = 'brown', width = 10)

text = forma.create_text(100,70,text = 'jCoders Academy bro!', fill = 'white', font = ('Arial',15))
rrethi = forma.create_oval(40,30,150,130, fill = 'purple', width = 5)

foto = PhotoImage(file = 'C:\\Users\\TechStore\\Downloads\\download.png')
pozicionimi = forma.create_image(150,150, image = foto)




forma1 = Canvas(dritare, bg = 'grey', width = 800, height = 800)
forma1.pack()
gjashtekendeshi = forma1.create_polygon(100,20,200,20,262,100,200,180,100,180,38,100, fill = 'blue', width = 10)
texti = forma1.create_text(150,100, text = 'jCoders Academy')

'''
lblx0 = Label(dritare, text = 'x0', bg = 'blue', fg = 'white', font = ('Arial',15,'bold'))
lbly0 = Label(dritare, text = 'y0', bg = 'orange', fg = 'black', font = ('Arial',15,'bold'))
lblx1 = Label(dritare, text = 'x1', bg = 'blue', fg = 'white', font = ('Arial',15,'bold'))
lbly1 = Label(dritare, text = 'y1', bg = 'orange', fg = 'black', font = ('Arial',15,'bold'))
lblx0.place(x = 15, y = 15, width = 50, height = 50)
lbly0.place(x = 15, y = 75, width = 50, height = 50)
lblx1.place(x = 15, y = 135, width = 50, height = 50)
lbly1.place(x = 15, y = 195, width = 50, height = 50)

tbx0 = Entry(dritare, font = ('Arial',15,'bold'))
tby0 = Entry(dritare, font = ('Arial',15,'bold'))
tbx1 = Entry(dritare, font = ('Arial',15,'bold'))
tby1 = Entry(dritare, font = ('Arial',15,'bold'))



tbx0.place(x = 75, y = 15, width = 100, height = 50)
tby0.place(x = 75, y = 75, width = 100, height = 50)
tbx1.place(x = 75, y = 135, width = 100, height = 50)
tby1.place(x = 75, y = 195, width = 100, height = 50)

canvas = Canvas(dritare, width = 400, height = 600, bg = 'grey')
canvas.place(x = 400, y = 0)

for i in range(0,25):
    canvas.create_line(0,25*i,400,25*i, fill = 'light grey')
for i in range(0,25):
    canvas.create_line(25*i,0,25*i,600,  fill='light grey')

lista = []

def butoniVizato():
    x0 = int(tbx0.get())
    y0 = int(tby0.get())
    x1 = int(tbx1.get())
    y1 = int(tby1.get())
    vija = canvas.create_line(x0,y0,x1,y1, fill = 'blue', width = 4)
    lista.append(vija)

def butoniPastro():
    for i in lista:
        canvas.delete(i)


vizato = Button(dritare, text = 'Çiz', bg = 'blue', fg = 'white', command = butoniVizato, font = ('Arial',20,'bold'))
pastro = Button(dritare, text = 'Temizle', bg = 'green', fg = 'white', command = butoniPastro, font = ('Arial',20,'bold'))

vizato.place(x = 15, y = 315, width = 100, height = 50)
pastro.place(x = 120, y = 315, width = 100, height = 50)


dritare.mainloop()