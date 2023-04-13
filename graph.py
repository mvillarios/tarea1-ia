# Funcion que carga el archivo y lo convierte en una matriz
def load_graph(file):
    matrix = []
    with open(file) as f:
        for line in f:
            matrix.append(line.split())
    
    return matrix

# Funcion que crea el grafo
def create_graph(data):
    nodes = {} # Inicializa el diccionario de nodos
    graph = {} # Inicializa el diccionario de aristas
    init = data[0][1] # Inicializa el nodo inicial
    goal = data[1][1] # Inicializa el nodo final
    
    # Crea el diccionario de nodos recorriendo la matriz
    for i in range(2, 10): 
        nodes[data[i][0]] = int(data[i][1])
    
    # Crea el diccionario de aristas recorriendo la matriz
    for i in range(10, len(data)):
        line = data[i][0].split(',') # Separa el nodo inicial y el nodo final de una arista
        if line[0] in graph: # Si el nodo inicial ya esta en el diccionario de aristas
            graph[line[0]][line[1]] = int(line[2]) # Agrega el nodo final y el peso de la arista
        else: # Si el nodo inicial no esta en el diccionario de aristas
            graph[line[0]] = {line[1]: int(line[2])} # Crea el nodo inicial y agrega el nodo final y el peso de la arista

    return init,goal,nodes,graph # Retorna el nodo inicial, el nodo final, el diccionario de nodos y el diccionario de aristas
    
