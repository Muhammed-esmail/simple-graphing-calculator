import random
import tkinter as tk
import time
import random as rand

linearbool = False
quadraticbool = True
bright_mode = True
dark_mode = False
graph = 0


def get_linear(linear):
    pass


def get_quadratic(quad):
    pass
def graph_quadratic(x_list, y_list, c):
    pass


output = ''
def input_from_buttons(inp):
    global output
    global text_result
    text_result.delete(1.0, "end")
    output += str(inp)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, output)
    return output
def call_after_output():
    global  output
    get_xy(output)
def delete():
    global text_result, output
    output = output[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0 , output)
def get_xy(function):
    x_list, y_list = [], []
    poly = False
    scale = 0.14
    root = False

    if  'x**' in function:
        poly = True
        if 'x**3' in function:
            scale /= 2
        if 'x**4' in function:
            scale = 0.05
        if 'x**1/2' in function or 'x**(1/2)' in function or 'x**0.5' in function or 'x**(0.5)' in function:
            poly = True
            scale = 45
            root = True





    for x in range(-300, 300):
        if root == True  :
            x = abs(x)
        x_list.append(x)
        if poly:
            x = x * scale
        try:
            y_list.append(eval(function))
        except ZeroDivisionError:
            y_list.append(99999)
    def get_c(function):
        try:
            x = 0
            c = eval(function)
        except:
            c = 0
        return c
    graph_quadratic(x_list,y_list,get_c(function))






def graph_quadratic(xlist,ylist,c):
    global canvas,graph,screen
    graph+=1
    random_color = ''
    colors = [
        "#800000",  # Maroon
        "#8B4513",  # Saddle Brown
        "#2F4F4F",  # Dark Slate Gray
        "#483D8B",  # Dark Slate Blue
        "#556B2F",  # Dark Olive Green
        "#800080",  # Purple
        "#808000",  # Olive
        "#2E8B57",  # Sea Green
        "#800000",  # Maroon
        "#8B0000",  # Dark Red
        "#483D8B",  # Dark Slate Blue
        "#2E8B57"  # Sea Green
    ]
    random_color = colors[random.randint(0,len(colors)-1)]


    if graph ==1:
        for i in range(0, len(xlist) - 1):
            time.sleep(0.005)
            canvas.create_line(249 + xlist[i], 249 - round(ylist[i], 5) - 50 * c,249 + xlist[i + 1], 249 - round(ylist[i], 5) - 50 * c,fill=random_color, width=2, tags="lines")
            screen.update()
    else:
        canvas.delete('lines')
        for i in range(0, len(xlist) - 1):
            time.sleep(0.005)
            canvas.create_line(249 + xlist[i], 249 - round(ylist[i], 5) - 50 * c, 249 + xlist[i + 1], 249 - round(ylist[i], 5) - 50 * c,fill=random_color, width=2, tags="lines")
            screen.update()

def dark_mode():
    global screen, btn_darkmode
    screen.configure(bg = "#1B1B1B")
    btn_darkmode.destroy()
def init_screen():
    global linearbool, linear, quadraticbool, quadratic, text_result, canvas, screen, btn_darkmode
    screen = tk.Tk()
    screen.title("Graph 2")
    if linearbool:
        screen.geometry("750x700")
        screen.grid()
    if quadraticbool:
        screen.geometry("780x700")
        screen.grid()
    canvas = tk.Canvas(width=500, height=500, background="white")
    canvas.grid(columnspan=13)
    if linearbool:
        text_result = tk.Text(screen, height=2, width=20, font=("Arial", 24))
        text_result.grid(columnspan=13, column=2, row=1)
    if quadraticbool:
        text_result = tk.Text(screen, height=2, width=20, font=("Arial", 24))
        text_result.grid(columnspan=10, column=4, row=1)

    btn_darkmode = tk.Button(width=20, height=3, text="switch to dark mode", command=dark_mode )
    btn_darkmode.grid(row=0 , column=15, columnspan=6)




    ix = iy = 0

    y1 = y2 = 0
    while y1 <= 500 and y2 <= 500:
        if iy != 5:
            canvas.create_line(0, y1, 500, y2, width=2)
        else:
            canvas.create_line(0, y1, 500, y2, width=2, fill="red")
        iy += 1
        y1 += 50
        y2 += 50
    x1 = x2 = 0
    while x1 <= 500 and x2 <= 500:
        if ix != 5:
            canvas.create_line(x1, 0, x2, 500, width=2)
        else:
            canvas.create_line(x1, 0, x2, 500, width=2, fill="red")
        ix += 1
        x1 += 50
        x2 += 50





    if linearbool:
        #buttons
        varcolor = 'green'
        numbercolor = 'lightblue'
        operatorcolor = 'purple'
        label_help = tk.Label(width=20, height=2, text="Type: a*x+b", )
        label_help.grid(row=1, column=0, columnspan=4)
        btn_x = tk.Button(width=5, height=5, command=lambda: input_from_buttons('x'), text="x", background=varcolor)
        btn_x.grid(row=2, column=1)
        btn_1 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('1'), text="1", background=numbercolor)
        btn_1.grid(row=2, column=2)
        btn_2 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('2'), text="2", background=numbercolor)
        btn_2.grid(row=2, column=3)
        btn_3 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('3'), text="3", background=numbercolor)
        btn_3.grid(row=2, column=4)
        btn_4 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('4'), text="4", background=numbercolor)
        btn_4.grid(row=2, column=5)
        btn_5 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('5'), text="5", background=numbercolor)
        btn_5.grid(row=2, column=6)
        btn_6 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('6'), text="6", background=numbercolor)
        btn_6.grid(row=2, column=7)
        btn_7 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('7'), text="7", background=numbercolor)
        btn_7.grid(row=2, column=8)
        btn_8 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('8'), text="8", background=numbercolor)
        btn_8.grid(row=2, column=9)
        btn_9 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('9'), text="9", background=numbercolor)
        btn_9.grid(row=2, column=10)
        btn_0 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('0'), text="0", background=numbercolor)
        btn_0.grid(row=2, column=11)
        btn_plus = tk.Button(width=5, height=5, command=lambda: input_from_buttons('+'), text="+",
                             background=operatorcolor)
        btn_plus.grid(row=2, column=12)
        btn_minus = tk.Button(width=5, height=5, command=lambda: input_from_buttons('-'), text="-",
                              background=operatorcolor)
        btn_minus.grid(row=2, column=13)
        btn_times = tk.Button(width=5, height=5, command=lambda: input_from_buttons('*'), text="*",
                              background=operatorcolor)
        btn_times.grid(row=2, column=14)
        btn_delete = tk.Button(width=5, height=5, command=delete, text="delete", background="red")
        btn_delete.grid(row=2, column=15)
        btn_GRAPH = tk.Button(width=5, height=5, command=call_after_output, text="Graph")
        btn_GRAPH.grid(row=2, column=16)
    if quadraticbool:
        #buttons here--------------------------
        varcolor = 'green'
        numbercolor = 'lightblue'
        operatorcolor = 'purple'
        label_help = tk.Label(width=20, height=2, text=f"Type: x**n for x\u207F", )
        label_help.grid(row=1,column=0,columnspan=5)
        btn_x = tk.Button(width=5, height=2, command=lambda: input_from_buttons('x'), text="x",background=varcolor)
        btn_x.grid(row=2, column=1)
        btn_1 = tk.Button(width=5, height=2, command=lambda: input_from_buttons('1'), text="1",background=numbercolor)
        btn_1.grid(row=2, column=2)
        btn_2 = tk.Button(width=5, height=2, command=lambda: input_from_buttons('2'), text="2",background=numbercolor)
        btn_2.grid(row=2, column=3)
        btn_3 = tk.Button(width=5, height=2, command=lambda: input_from_buttons('3'), text="3",background=numbercolor)
        btn_3.grid(row=2, column=4)
        btn_4 = tk.Button(width=5, height=2, command=lambda: input_from_buttons('4'), text="4",background=numbercolor)
        btn_4.grid(row=2, column=5)
        btn_5 = tk.Button(width=5, height=2, command=lambda: input_from_buttons('5'), text="5",background=numbercolor)
        btn_5.grid(row=2, column=6)
        btn_6 = tk.Button(width=5, height=2, command=lambda: input_from_buttons('6'), text="6",background=numbercolor)
        btn_6.grid(row=2, column=7)
        btn_7 = tk.Button(width=5, height=2, command=lambda: input_from_buttons('7'), text="7",background=numbercolor)
        btn_7.grid(row=2, column=8)
        btn_8 = tk.Button(width=5, height=2, command=lambda: input_from_buttons('8'), text="8",background=numbercolor)
        btn_8.grid(row=2, column=9)
        btn_9 = tk.Button(width=5, height=2, command=lambda: input_from_buttons('9'), text="9",background=numbercolor)
        btn_9.grid(row=2, column=10)
        btn_0 = tk.Button(width=5, height=2, command=lambda: input_from_buttons('0'), text="0", background=numbercolor)
        btn_0.grid(row=2, column=11)
        btn_dot = tk.Button(width=5, height=2, command=lambda: input_from_buttons('.'), text="point", background=varcolor)
        btn_dot.grid(row=2, column=12)
        btn_plus = tk.Button(width=5, height=2, command=lambda: input_from_buttons('+'), text="+", background=operatorcolor)
        btn_plus.grid(row=2, column=13)
        btn_minus = tk.Button(width=5, height=2, command=lambda: input_from_buttons('-'), text="-", background=operatorcolor)
        btn_minus.grid(row=2, column=14)
        btn_times = tk.Button(width=5, height=2, command=lambda: input_from_buttons('*'), text="*", background=operatorcolor)
        btn_times.grid(row=2, column=15)
        btn_division = tk.Button(width=5, height=2, command=lambda: input_from_buttons('/'), text="/",background=operatorcolor)
        btn_division.grid(row=3, column=1)
        btn_delete = tk.Button(width=5, height=2, command=delete, text="delete",background="red")
        btn_delete.grid(row=3, column=2)
        btn_GRAPH = tk.Button(width=5, height=2, command=call_after_output, text="Graph", background="blue")
        btn_GRAPH.grid(row=3, column=3)

        btn_parantheses_open = tk.Button(width=5, height=2, command=lambda: input_from_buttons('('), text="(",background=operatorcolor)
        btn_parantheses_open.grid(row=2, column=16)
        btn_parantheses_closed = tk.Button(width=5, height=2, command=lambda: input_from_buttons(')'), text=")",background=operatorcolor)
        btn_parantheses_closed.grid(row=2, column=17)

        # buttons here--------------------------


    screen.update()
    screen.mainloop()


init_screen()

