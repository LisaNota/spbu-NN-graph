import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class GraphGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Поиск кратчайшего пути методом ближайшего соседа")
        self.root.geometry('800x500')
        
        self.create_frames()
        self.create_graph()
        self.create_settings()

    def create_frames(self):
        self.canvas = tk.Canvas(self.root, width=1000, height=1000, borderwidth=0, highlightthickness=0)
        self.canvas.place(relx=0, rely=0.0)

        self.line1 = self.canvas.create_line(350, 240, 800, 240)
        self.line2 = self.canvas.create_line(350, 0, 350, 500)

    def create_graph(self):
        self.fig, self.ax = plt.subplots(figsize=(3.5, 1.8))
        self.ax.set_facecolor('white')
        self.ax.set_axis_off()

        self.canvas_widget = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_widget.get_tk_widget().place(relx=0.5, rely=0.08)

    def set_calculating_command(self, calculating_command):
        self.calculating_command = calculating_command
        
    def set_creating_command(self, creating_command):
        self.creating_command = creating_command
        
    def create_settings(self):
        self.lbl = tk.Label(self.root, text="Параметры входного графа", font=("Arial", 11))
        self.lbl.place(relx=0.1, rely=0.01)

        self.lblfunc = tk.Label(self.root, text="Количество вершин:", font=("Arial", 10))
        self.lblfunc.place(relx=0.027, rely=0.075)

        self.cnt_vertices = tk.Spinbox(self.root, from_=2, to=10, width=5)
        self.cnt_vertices.place(relx=0.32, rely=0.08)

        lbl3 = tk.Label(self.root, text="Вводите взвешенные ребра в формате:", font=("Arial", 10))
        lbl3.place(relx=0.027, rely=0.12)

        lbl_1 = tk.Label(self.root, text="(1, 2, 3); (2, 1, 8)", font=("Arial", 10))
        lbl_1.place(relx=0.027, rely=0.16)

        lbl_2 = tk.Label(self.root, text="где первые два числа - вершины,", font=("Arial", 10))
        lbl_2.place(relx=0.027, rely=0.2)

        lbl_3 = tk.Label(self.root, text="а третье - длина ребра", font=("Arial", 10))
        lbl_3.place(relx=0.027, rely=0.24)

        txt_edges = tk.Text(self.root, width=37, height=5)  
        txt_edges.place(relx=0.027, rely=0.29)  

        but = tk.Button(self.root, text="Создать граф", width=42, 
                        command=lambda: self.creating_command(
                            int(self.cnt_vertices.get()), txt_edges.get("1.0", tk.END)),
                        bg="#DDDDDD", activebackground="#CCCCCC", relief=tk.GROOVE)
        but.place(relx=0.027, rely=0.5)

        lbl5 = tk.Label(self.root, text="Полученный путь", font=("Arial", 10))
        lbl5.place(relx=0.027, rely=0.64)

        txt_1edges = tk.Text(self.root, width=37, height=3, state='disabled', background='#EAEAEA', fg="black")
        txt_1edges.place(relx=0.027, rely=0.7)  

        lbl_5 = tk.Label(self.root, text="Длина пути", font=("Arial", 10))
        lbl_5.place(relx=0.027, rely=0.82)

        txt_2edges = tk.Text(self.root, width=37, 
                             height=1, state='disabled',background='#EAEAEA',  fg="black")
        txt_2edges.place(relx=0.027, rely=0.88)  

        txt_1edges = tk.Text(self.root, width=37, height=3, state='disabled', background='#EAEAEA', fg="black")
        txt_1edges.place(relx=0.027, rely=0.7)  

        self.lbl6 = tk.Label(self.root, text="Исходный граф", font=("Arial", 11))
        self.lbl6.place(relx=0.64, rely=0.01)

        self.lbl6 = tk.Label(self.root, text="Выходной граф", font=("Arial", 11))
        self.lbl6.place(relx=0.64, rely=0.515)

        self.fig_2, self.ax_2 = plt.subplots(figsize=(3.5, 1.8))
        self.ax_2.set_facecolor('white')
        self.ax_2.set_axis_off()

        self.canvas_widget_2 = FigureCanvasTkAgg(self.fig_2, master=self.root)
        self.canvas_widget_2.get_tk_widget().place(relx=0.5, rely=0.58)
        
        but_2 = tk.Button(self.root, text="Вычислить оптимальный путь", width=42,
                          command=lambda: self.calculating_command(
                              int(self.cnt_vertices.get()), txt_edges.get("1.0", tk.END), 
                              txt_2edges, txt_1edges),
                          bg="#DDDDDD", activebackground="#CCCCCC", relief=tk.GROOVE)
        but_2.place(relx=0.027, rely=0.57)
