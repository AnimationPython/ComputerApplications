import Tkinter

main_window = Tkinter.Tk()

def exit():
    main_window.destroy()
    
button = Tkinter.Button(text = "click me", command=exit )
button.pack()

canvas = Tkinter.Canvas(width=500, height=500)
canvas.pack()
canvas.create_oval(50,50, 300,600)

def clear_canvas():
    canvas.delete(Tkinter.ALL)
clear_button = Tkinter.Button(text = "clear", command = clear_canvas)
clear_button.pack()

main_window.mainloop()
