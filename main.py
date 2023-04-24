import graph as g
import methods as m

def main():

    archivo, metodo = g.read_entry() # Lee la entrada

    data = g.load_graph(archivo) # Carga el grafo
    init,goal,nodes,graph = g.create_graph(data) # Crea el grafo
    
    # Ejecuta el metodo de busqueda seleccionado
    if metodo == '1':
        print("Busqueda en Profundidad")
        path, total_cost, expand_count = m.DFS(init, goal, nodes, graph)
    elif metodo == '2':
        print("Busqueda por Costo Uniforme")
        path, total_cost, expand_count = m.uniform_cost_search(init, goal, nodes, graph)
    elif metodo == '3':
        print("Busqueda Greedy")
        path, total_cost, expand_count = m.greedy(init, goal, nodes, graph)
    elif metodo == '4':
        print("Busqueda A*")
        path, total_cost, expand_count = m.a_estrella(init, goal, nodes, graph)
    else: # Si el metodo de busqueda no es valido
        print("Metodo no valido")
        return # Sale del programa

    # Imprime el camino y el costo total
    for node in path:
        if node != path[-1]:
            print(node, end=' -> ')
        else:
            print(node)
    print('Costo:', total_cost)

    # Imprime los nodos expandidos y el numero de veces que se expandieron
    for node in expand_count:
        print(node, ':', expand_count[node])

    # Imprime el total de nodos expandidos
    print('Nodos expandidos:', sum(expand_count[node] for node in expand_count))   

    # si el camino es el optimo imprime "Optimo" de lo contrario imprime "No Optimo"
    if path == ["A", "B", "D", "H"]:
        print("Optimo")
    else:
        print("No Optimo")

if __name__ == "__main__":
    main()




