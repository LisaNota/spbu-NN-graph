import tkinter as tk
from graph_gui import GraphGUI
import networkx as nx
from matplotlib.axes import Axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

options = {
    'node_color': '#D3D3D3',
    'node_size': 300,
    'width': 1,
    'arrowstyle': '-|>',
    'arrowsize': 10,
    'edge_color': 'black',
    'font_size': 12,
}
pos = None

def creating(cnt_vertices: int, edges: str, ax, canvas_widget) -> None:
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
    global options, pos

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


def nearest_neighbour(cnt_vertices, edges, txt_len, txt_way, ax_2, canvas_widget_2) -> None:
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
    global options, pos

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


def main():
    root = tk.Tk()
    app = GraphGUI(root)
    app.set_calculating_command(lambda cnt_vertices, edges, txt_len, txt_way: nearest_neighbour(
        cnt_vertices, edges, txt_len, txt_way, app.ax_2, app.canvas_widget_2))
    app.set_creating_command(lambda cnt_vertices, edges: creating(cnt_vertices, edges, app.ax, app.canvas_widget))

    root.mainloop()

if __name__ == "__main__":
    main()
