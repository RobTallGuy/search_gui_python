import tkinter as tk
from tkinter import *
from bfs import *
import time



root = Tk()

root.geometry('{}x{}'.format(500, 500))

root.title("Search")

all_points = [[0 for x in range(10)] for y in range(10)]
all_walls = set()

square = Canvas(root, width=500, height=500)
square_size = 50
canvas_size = 500

#printing grid of squares

for y in range(canvas_size):
    for x in range(canvas_size):
        if x%square_size == 0 and y%square_size == 0:
            all_points[int(x/square_size)][int(y/square_size)] = int(x/50), int(y/50)
            # print(f'{int(x/50)}, {int(y/50)}')
            square.create_rectangle(x, y, x+square_size, y+square_size, fill='black', outline='white', tags='{},{}'.format(x,y))
            # square.create_text((x+int(square_size/2), y+int(square_size/2)), text='{},{}'.format(x, y), fill='white')
square.pack(expand=True)  

def round_down(number, divisor):
    return (number - (number%divisor))

def noNothing():
    print("woot, nothing")

starting_coord = StringVar()
finishing_coord = StringVar()

def drawBlue(i):
    square.itemconfig(square.find_closest((i[0] * square_size), (i[1] * square_size)), fill='blue')

def start_this():
    print(all_walls)
    if starting_coord.get() != '':
        st_ar = starting_coord.get().split(',')
        st_co = ((int(st_ar[0])), (int(st_ar[1])))
        fi_ar = finishing_coord.get().split(',')
        fi_co = ((int(fi_ar[0])), (int(fi_ar[1])))
        bfs = Bfs(st_co, fi_co, all_points, square, square_size, all_walls)
        path = bfs.solve()
        for i in path[1:-1]:
            drawBlue(i)
            # root.after(3000, drawBlue(i))
        

def two_points():
    # print("hi")
    window = Toplevel(root)
    start_text = Label(window, text='start(x,y)')
    start_text.pack()
    # starting_coord = StringVar()
    start_value = Entry(window, textvariable=starting_coord, bd=1)
    start_value.pack()

    finish_text = Label(window, text='start(x,y)')
    finish_text.pack()
    # finishing_coord = StringVar()
    finish_value = Entry(window, textvariable=finishing_coord, bd=1)
    finish_value.pack()

    def close_and_save():
        window.destroy()
        starting_points = (starting_coord.get()).split(',')
        finishing_points = (finishing_coord.get()).split(',')
        square.itemconfig(square.find_closest((int(starting_points[0]) * square_size), (int(starting_points[1]) * square_size)), fill='pink')
        square.itemconfig(square.find_closest((int(finishing_points[0]) * square_size), (int(finishing_points[1]) * square_size)), fill='pink')

    b = tk.Button(window, text='Save', command=close_and_save)

    b.pack(side=BOTTOM)
    

#Layout for menu
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Search type', menu=subMenu)
subMenu.add_checkbutton(label='A* Search', command=noNothing)
subMenu.add_checkbutton(label='Breadth-First Search', command=noNothing)
menu.add_command(label='Points', command=two_points)
menu.add_command(label='Start', command=start_this)


#functions for clicking a square


def click(event):
    if square.find_withtag(CURRENT):
        # square.itemconfig(CURRENT, fill='green')
        print(event)



def unclick(event):
    # square.itemconfigure(square.find_closest(round_down(event.x, 50), round_down(event.x, 50)), fill='green')
    print(event)

def coords(event):
    square.itemconfig(square.find_closest(round_down(event.x, square_size), round_down(event.y, square_size)), fill='green')
    print(f'{int(round_down(event.x, square_size)/square_size)}, {int(round_down(event.y, square_size)/square_size)}')
    all_walls.add((int(round_down(event.x, square_size)/square_size), int(round_down(event.y, square_size)/square_size)))
    # print(f'{round_down(event.x, square_size)}, {round_down(event.y, square_size)}, {CURRENT}')
    # square.itemconfig(199, fill='blue')

        


            

square.bind("<Button-1>", click)
square.bind("<ButtonRelease-1>", unclick)
square.bind("<B1-Motion>", coords)

root.mainloop()


"""
So I have the bfs attempting to work, but I don't like how the fill with squares interact
It's grabbing the nearest one, and sometimes that's too big of one to work, I think anyway.
I could try putting a delay on it, which would solve many of the problem?
"""