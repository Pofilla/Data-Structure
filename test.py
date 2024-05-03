import networkx as nx
import matplotlib.pyplot as plt

def prim(graph):
    V = len(graph)
    G = nx.Graph()

    selected = [0] * V
    no_edge = 0
    selected[0] = True

    while no_edge < V - 1:
        minimum = float('inf')
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j] and minimum > graph[i][j]:
                        minimum = graph[i][j]
                        x = i
                        y = j

        print(str(x) + "-" + str(y) + ":" + str(graph[x][y]))
        G.add_edge(x, y, weight=graph[x][y])
        selected[y] = True
        no_edge += 1

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()

graph_input = []
while True:
    row_input = input("Enter row of the graph (type 'done' when finished): ")
    if row_input.lower() == 'done':
        break
    graph_input.append([int(weight) for weight in row_input.split()])

prim(graph_input)