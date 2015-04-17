import Tkinter
main_window=Tkinter.Tk()
def click():
    print 'Error 404'
Button = Tkinter.Button(main_window,text = 'python', command=click)
Button.pack()
canvas=Tkinter.Canvas(main_window , width= 500 , height=700)
canvas.pack()
canvas.create_oval(10,10,50,600)
def clear():
    canvas.delete(Tkinter.ALL)
button2=Tkinter.Button(main_window, text= 'clear', command=clear)
button2.pack()
main_window.mainloop()
