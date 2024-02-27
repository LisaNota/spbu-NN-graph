import numpy as np
import networkx as nx
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

options = {
    'node_color': '#D3D3D3',     # color of node
    'node_size': 300,          # size of node
    'width': 1,                 # line width of edges
    'arrowstyle': '-|>',        # array style for directed graph
    'arrowsize': 10,            # size of arrow
    'edge_color':'black',       # edge color
    'font_size': 12,            # size of font
}


def creating(cnt_vertices: int, edges: str) -> None:
    """
    Creates and displays a graph based on the provided vertices and edges.

    Parameters:
    cnt_vertices (int): The number of vertices in the graph.
    edges (str): A string containing the edges of the graph in the format 
                 "(vertex_1, vertex_2, weight); (vertex_1, vertex_2, weight); ...".
                  Delimiters between edges are semicolons (;).

    Returns:
    None
    """
    global ax, canvas_widget, pos, options

    edges = ''.join(edges).split(';')
    edges = [edge.strip() for edge in edges]
    weighted_edges = [eval(edge) for edge in edges]
    vertices = list(range(cnt_vertices))
    
    G = nx.DiGraph(directed=True)
    G.add_nodes_from(vertices)
    G.add_weighted_edges_from(weighted_edges)

    pos = nx.circular_layout(G)
    nx.draw(G, ax=ax, pos=pos, with_labels=True, arrows=True, **options)

    canvas_widget.draw()


  def nearest_neighbour(cnt_vertices: int, edges: str, txt_len: tk.Text, txt_way: tk.Text) -> None:
    """
    Finds the approximate shortest path using the nearest neighbor heuristic and displays the result.

    Parameters:
    cnt_vertices (int): The number of vertices in the graph.
    edges (str): A string containing the edges of the graph in the format "vertex_1, vertex_2, weight; vertex_1, vertex_2, weight; ...".
                  Delimiters between edges are semicolons (;).
    txt_len (tk.Text): A Text widget where the length of the found path will be displayed.
    txt_way (tk.Text): A Text widget where the found path will be displayed.

    Returns:
    None
    """
    global ax_2, canvas_widget_2, pos, options
    
    nodes = [vertice for vertice in range(cnt_vertices)]
    edges = ''.join(edges).split(';')
    edges = [edge.strip() for edge in edges]
    weighted_edges = [eval(edge) for edge in edges]
    
    ANS_LEN = float('inf')
    ANS_CYCLE = []
    
    for started_id in range(cnt_vertices):
        summ = 0
        curr = nodes[started_id]
        completed = [curr]

        for i in range(cnt_vertices-1):
            result = float('inf')
            for edge in weighted_edges:
                if edge[0] == curr and edge[1] not in completed and edge[2] < result:
                        result = edge[2]
                        new_vert = edge[1]
            completed.append(new_vert)
            summ += result
            curr = new_vert

        flag = False
        for edge in weighted_edges:
            if edge[0] == completed[0] and edge[1] == completed[-1]:
                summ += edge[2]
                flag = True
                break

        if summ < ANS_LEN:
            ANS_LEN = summ
            ANS_CYCLE = completed

    txt_len.config(state='normal')
    txt_len.insert(tk.END, ANS_LEN)
    txt_len.config(state='disabled')

    txt_way.config(state='normal')
    txt_way.insert(tk.END, ANS_CYCLE)
    txt_way.config(state='disabled')
    
    F = nx.DiGraph(directed=True)
    ANS_CYCLE.append(ANS_CYCLE[0])
    F.add_nodes_from(ANS_CYCLE)
    
    for i in range(len(ANS_CYCLE)-1):
        F.add_edge(ANS_CYCLE[i], ANS_CYCLE[i+1])

    nx.draw(F, ax=ax_2, pos=pos, with_labels=True, arrows=True, **options)

    canvas_widget_2.draw()


root = tk.Tk()
root.title("Поиск кратчайшего пути методом ближайшего соседа")
root.geometry('800x500')

#####     Frames    ######

canvas = tk.Canvas(root, width=1000, height=1000, borderwidth=0, highlightthickness=0)
canvas.place(relx=0, rely=0.0)

line1 = canvas.create_line(350, 240, 800, 240)
line2 = canvas.create_line(350, 0, 350, 500)

#####    Graph    #####

fig, ax = plt.subplots(figsize=(3.5, 1.8))
ax.set_facecolor('white')
ax.set_axis_off()

canvas_widget = FigureCanvasTkAgg(fig, master=root)
canvas_widget.get_tk_widget().place(relx=0.5, rely=0.08)

##### Settings #####

lbl = tk.Label(root, text="Параметры входного графа", font=("Arial", 11) )
lbl.place(relx=0.1, rely=0.01)

lblfunc = tk.Label(root, text="Количество вершин:", font=("Arial", 10))
lblfunc.place(relx=0.027, rely=0.075)

cnt_vertices = tk.Spinbox(root, from_=2, to=10, width=5)
cnt_vertices.place(relx=0.32, rely=0.08)

lbl3 = tk.Label(root, text="Вводите взвешенные ребра в формате:", font=("Arial", 10))
lbl3.place(relx=0.027, rely=0.12)

lbl_1 = tk.Label(root, text="(1, 2, 3); (2, 1, 8)", font=("Arial", 10))
lbl_1.place(relx=0.027, rely=0.16)

lbl_2 = tk.Label(root, text="где первые два числа - вершины,", font=("Arial", 10))
lbl_2.place(relx=0.027, rely=0.2)

lbl_3 = tk.Label(root, text="а третье - длина ребра", font=("Arial", 10))
lbl_3.place(relx=0.027, rely=0.24)

txt_edges = tk.Text(root, width=37, height=5)  
txt_edges.place(relx=0.027, rely=0.29)  

but = tk.Button(root, text="Создать граф", width=42, 
                command=lambda: creating(int(cnt_vertices.get()), txt_edges.get("1.0", tk.END)),
                bg="#DDDDDD", activebackground="#CCCCCC", relief=tk.GROOVE)
but.place(relx=0.027, rely=0.5)

lbl5 = tk.Label(root, text="Полученный путь", font=("Arial", 10))
lbl5.place(relx=0.027, rely=0.64)

txt_1edges = tk.Text(root, width=37, height=3, state='disabled', background='#EAEAEA', fg="black")
txt_1edges.place(relx=0.027, rely=0.7)  

lbl_5 = tk.Label(root, text="Длина пути", font=("Arial", 10))
lbl_5.place(relx=0.027, rely=0.82)

txt_2edges = tk.Text(root, width=37, height=1, state='disabled',background='#EAEAEA',  fg="black")
txt_2edges.place(relx=0.027, rely=0.88)  

txt_1edges = tk.Text(root, width=37, height=3, state='disabled', background='#EAEAEA', fg="black")
txt_1edges.place(relx=0.027, rely=0.7)  

but_2 = tk.Button(root, text="Вычислить оптимальный путь", width=42, 
                command=lambda: nearest_neighbour(int(cnt_vertices.get()), txt_edges.get("1.0", tk.END), txt_2edges, txt_1edges), 
                bg="#DDDDDD", activebackground="#CCCCCC", relief=tk.GROOVE)
but_2.place(relx=0.027, rely=0.57)

#####  Result  ######

lbl6 = tk.Label(root, text="Исходный граф", font=("Arial", 11))
lbl6.place(relx=0.64, rely=0.01)

lbl6 = tk.Label(root, text="Выходной граф", font=("Arial", 11))
lbl6.place(relx=0.64, rely=0.515)

fig_2, ax_2 = plt.subplots(figsize=(3.5, 1.8))
ax_2.set_facecolor('white')
ax_2.set_axis_off()

canvas_widget_2 = FigureCanvasTkAgg(fig_2, master=root)
canvas_widget_2.get_tk_widget().place(relx=0.5, rely=0.58)

#####################

root.mainloop()

