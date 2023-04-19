import graph as g
import methods as m

def main():
    data = g.load_graph('graph.txt')
    init,goal,nodes,graph = g.create_graph(data)

    #path, total_cost, expand_count = m.DFS(init, goal, nodes, graph)

    path, total_cost, expand_count = m.a_estrella(init, goal, nodes, graph)

    for node in path:
        if node != path[-1]:
            print(node, end=' -> ')
        else:
            print(node)

    print('Costo:', total_cost)

    # Imprime los nodos expandidos y el numero de veces que se expandieron
    for node in expand_count:
        print(node, ':', expand_count[node])
            
if __name__ == "__main__":
    main()




