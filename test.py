from tkinter import *

btn1 = {}
btn2 = {}

# create the canvas, size in pixels
canvas = Canvas(width=300, height=200, bg='white')

# pack the canvas into a frame/form
canvas.pack(expand=YES, fill=BOTH)

def drag(event):
    print(vars(event))
    # event.widget.place(x=event.x_root, y=event.y_root,anchor=CENTER)
    canvas.move("andgate", event.x_root, event.y_root)
    # canvas.move(btn1, event.x_root + 70, event.y_root - 25)
    # canvas.move(btn2, event.x_root + 70, event.y_root + 5)

def moveANDGate(event, tag):
    print('MOVEUUUUU')
    x=event.x
    y=event.y
    coords=canvas.coords(tag)
    movex=x-coords[0]
    movey=y-coords[1]
    canvas.move(tag, movex, movey)

def moveANDGate(event):
    # x=event.x
    # y=event.y
    print(vars(event))
    # coords=canvas.coords("andgate")
    # movex=x-coords[0]
    # movey=y-coords[1]
    # canvas.move("andgate", movex, movey)
    # canvas.move('andgate', x, y)
    canvas.move('andgate', event.x, event.y)

# load the .gif image file
gif1 = PhotoImage(file="icons/laptop-back.png")
label = Label(image=gif1, bg='white')
label.bind("<B1-Motion>", moveANDGate)

# image_id = canvas.create_image(50, 50, image=gif1, tag="andgate")
# canvas.tag_bind(image_id, "<B1-Motion>", moveANDGate)

button1 = Button(width=20, height=20, image=gif1)
button1.bind("<B1-Motion>", moveANDGate)

button2 = Button(width=20, height=20, image=gif1)
button2.bind("<B1-Motion>", moveANDGate)

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
# canvas.create_image(50, 50, image=gif1, tag="andgate")
canvas.create_window(50, 50, window=label, tag="andgate")
canvas.create_window(120, 25, window=button1, tag="andgate")
canvas.create_window(120, 55, window=button2, tag="andgate")
# canvas.tag_bind("andgate", "<B1-Motion>", lambda event, tag="andgate": moveANDGate(event, tag))
# canvas.tag_bind('andgate', "<B1-Motion>", moveANDGate)



# run it ...
mainloop()
