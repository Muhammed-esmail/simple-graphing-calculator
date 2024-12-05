import tkinter as tk
import time
linearbool = False
quadraticbool = False
graph = 0

equation_type = input("Choose equation type (linear = 1, quadratic = 2): ")
if equation_type == "1":
    linearbool = True
if equation_type == "2":
    quadraticbool = True
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
    if linearbool:
        get_linear(output)
    if quadraticbool:
        get_quadratic(output)
def delete():
    global text_result, output
    output = output[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0 , output)


def get_linear(line):
    def get_a(line):
        t1 = ''
        t1 = line.replace('x', '1')
        t1 = t1 + f"-{get_b(line)}"
        a = eval(t1)
        return a

    def get_b(line):
        t2 = ''
        t2 = line.replace('x', '0')
        b = eval(t2)
        return b
    a = get_a(line)
    b = get_b(line)
    y_list ,x_list = [] , []
    for i in range(-1000, 1000):
        x_list.append(i)
        y_list.append(a * i + b)
    graph_linear(x_list,y_list,b)
    # a = line.split(x)
    return x_list, y_list, b


def get_quadratic(quad):
    # as+bx+c
    global output

    def get_a(quad):
        t1 = ''
        t1 = quad.replace('x', '0')
        t1 = t1.replace('s', '1')
        t1 = t1 + f'-{get_c(quad)}'
        a = eval(t1)
        return a

    def get_c(quad):
        t2 = ''
        t2 = quad.replace('x', '0')
        t2 = t2.replace('s', '0')
        c = eval(t2)
        return c

    def get_b(quad):
        t3 = ''
        t3 = quad.replace('s', '0')
        t3 = t3.replace('c', '0')
        t3 = t3.replace('x', '1')
        t3 = t3 + f'-{get_c(quad)}'
        b = eval(t3)
        return b
    a = get_a(quad)
    b = get_b(quad)
    c = get_c(quad)
    x_list = []
    y_list = []
    scale = 0.14
    if a == 0:
        scale = 1
    for i in range(-500, 500):
        x_list.append(i)  # Adjust the scaling factor (0.5 in this example)
        y_list.append(a * (scale * i) ** 2 + b * (scale * i) + c)  # Apply the same scaling factor to x^2 and x terms
    graph_quadratic(x_list,y_list,c)
    return x_list, y_list, c

def graph_linear(xlist, ylist , c):
    global canvas, graph,screen
    graph +=1
    if graph == 1:
        for i in range(len(xlist)-1):
            time.sleep(0.001)
            canvas.create_line(249 + xlist[i], 249 - ylist[i] - 50 * c, 249 + xlist[i + 1], 249 - ylist[i + 1] - 50 * c,fill="green", width=2, tags="lines")
            screen.update()
    else:
        canvas.delete('lines')
        for i in range(0, len(xlist) - 1):
            time.sleep(0.001)
            canvas.create_line(249 + xlist[i], 249 - ylist[i] - 50 * c, 249 + xlist[i + 1], 249 - ylist[i + 1] - 50 * c,
                               fill="green", width=2, tags="lines")
            screen.update()

def graph_quadratic(xlist,ylist,c):
    global canvas,graph,screen
    graph+=1
    if graph ==1:
        for i in range(0, len(xlist) - 1):
            time.sleep(0.001)
            canvas.create_line(249 + xlist[i], 249 - ylist[i] - 50 * c,249 + xlist[i + 1], 249 - ylist[i + 1] - 50 * c,fill="green", width=2, tags="lines")
            screen.update()
    else:
        canvas.delete('lines')
        for i in range(0, len(xlist) - 1):
            time.sleep(0.001)
            canvas.create_line(249 + xlist[i], 249 - ylist[i] - 50 * c, 249 + xlist[i + 1], 249 - ylist[i + 1] - 50 * c,fill="green", width=2, tags="lines")
            screen.update()
def init_screen():
    global linearbool, linear, quadraticbool, quadratic, text_result, canvas, screen
    screen = tk.Tk()
    screen.title("Graphs")
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
        text_result.grid(columnspan=10, column=2, row=1)



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
        label_help = tk.Label(width=20, height=2, text="Type: a*s+b*x+c|s = x^2", )
        label_help.grid(row=1,column=0,columnspan=3)
        btn_s = tk.Button(width=5, height=5, command=lambda: input_from_buttons('s'), text="s", background=varcolor)
        btn_s.grid(row=2, column=0, )
        btn_x = tk.Button(width=5, height=5, command=lambda: input_from_buttons('x'), text="x",background=varcolor)
        btn_x.grid(row=2, column=1)
        btn_1 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('1'), text="1",background=numbercolor)
        btn_1.grid(row=2, column=2)
        btn_2 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('2'), text="2",background=numbercolor)
        btn_2.grid(row=2, column=3)
        btn_3 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('3'), text="3",background=numbercolor)
        btn_3.grid(row=2, column=4)
        btn_4 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('4'), text="4",background=numbercolor)
        btn_4.grid(row=2, column=5)
        btn_5 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('5'), text="5",background=numbercolor)
        btn_5.grid(row=2, column=6)
        btn_6 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('6'), text="6",background=numbercolor)
        btn_6.grid(row=2, column=7)
        btn_7 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('7'), text="7",background=numbercolor)
        btn_7.grid(row=2, column=8)
        btn_8 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('8'), text="8",background=numbercolor)
        btn_8.grid(row=2, column=9)
        btn_9 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('9'), text="9",background=numbercolor)
        btn_9.grid(row=2, column=10)
        btn_0 = tk.Button(width=5, height=5, command=lambda: input_from_buttons('0'), text="0", background=numbercolor)
        btn_0.grid(row=2, column=11)
        btn_plus = tk.Button(width=5, height=5, command=lambda: input_from_buttons('+'), text="+", background=operatorcolor)
        btn_plus.grid(row=2, column=12)
        btn_minus = tk.Button(width=5, height=5, command=lambda: input_from_buttons('-'), text="-", background=operatorcolor)
        btn_minus.grid(row=2, column=13)
        btn_times = tk.Button(width=5, height=5, command=lambda: input_from_buttons('*'), text="*", background=operatorcolor)
        btn_times.grid(row=2, column=14)
        btn_delete = tk.Button(width=5, height=5, command=delete, text="delete",background="red")
        btn_delete.grid(row=2, column=15)
        btn_GRAPH = tk.Button(width=5, height=5, command=call_after_output, text="Graph", background="blue")
        btn_GRAPH.grid(row=2, column=16)

        # buttons here--------------------------


    screen.update()
    screen.mainloop()


init_screen()

