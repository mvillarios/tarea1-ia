import random    

def DFS(init, goal, nodes, graph):
    
    lista_nodos = [(init, 0, [init])] # Lista de nodos a expandir guarda el nodo actual, el costo total, y el camino

    expand_count = {node: 0 for node in nodes} # Diccionario que guarda el numero de veces que se expande cada nodo

    visited = set() # Conjunto de nodos visitados

    while lista_nodos: # Mientras la lista de nodos a expandir no este vacia

        node, costo, camino = lista_nodos.pop(random.randint(0, len(lista_nodos)-1)) # Obtiene un nodo random de la lista

        if node == goal: # Si el nodo es el objetivo, retorna el camino y el costo
            return camino, costo, expand_count

        visited.add(node) # Agrega el nodo a los visitados

        expand_count[node] += 1 # Incrementa el numero de veces que se expande el nodo
        for vecino in graph[node]: # Para cada vecino del nodo actual
            if vecino not in visited: # Si el vecino no ha sido visitado
                costo_total = costo + graph[node][vecino] # Calcula el costo que se llevaba mas el costo del vecino
                camino_nuevo = camino.copy() + [vecino] # Crea un nuevo camino con el camino actual mas el vecino
                nodo_nuevo = (vecino, costo_total, camino_nuevo) # Crea un nuevo nodo con el vecino, el costo y el camino
                lista_nodos.append(nodo_nuevo) # Agrega el nodo a la lista de nodos a expandir
                
def uniform_cost_search(init, goal, nodes, graph):

    lista_nodos = [(init, 0, [init])] # Lista de nodos a expandir guarda el nodo actual, el costo total, y el camino

    expand_count = {node: 0 for node in nodes} # Diccionario que guarda el numero de veces que se expande cada nodo

    while lista_nodos: # Mientras la lista de nodos a expandir no este vacia

        # Ordena la lista de nodos por costo
        lista_nodos.sort(key=lambda x: x[1])

        # Obtiene el nodo con menor costo
        node, costo, camino = lista_nodos.pop(0)

        # Si el nodo es el objetivo, retorna el camino y el costo
        if node == goal:
            return camino, costo, expand_count

        expand_count[node] += 1 # Incrementa el numero de veces que se expande el nodo
        for vecino in graph[node]: # Para cada vecino del nodo actual
            
            costo_total = costo + graph[node][vecino] # Calcula el costo que se llevaba mas el costo del vecino
            camino_nuevo = camino.copy() + [vecino] # Crea un nuevo camino con el camino actual mas el vecino
            nodo_nuevo = (vecino, costo_total, camino_nuevo) # Crea un nuevo nodo con el vecino, el costo y el camino

            lista_nodos.append(nodo_nuevo) # Agrega el nodo a la lista de nodos a expandir

def greedy(init, goal, nodes, graph):

    node = init # Nodo actual
    path = [node] # Camino

    costo_total = 0 # Costo total

    expand_count = {node: 0 for node in nodes} # Diccionario que guarda el numero de veces que se expande cada nodo

    # Mientras el nodo actual tenga hijos
    while graph[node]:

        expand_count[node] += 1
        # Obtiene el nodo con menor costo heuristico
        node = min(graph[node], key=lambda x: nodes[x])

        # Si el nodo es el objetivo, retorna el camino y el costo
        if node == goal:
            path.append(node)
            costo_total += graph[path[-2]][node]
            return path, costo_total, expand_count

        path.append(node) # Agrega el nodo al camino
        costo_total += graph[path[-2]][node] # Incrementa el costo total


def a_estrella(init, goal, nodes, graph):

    lista_nodos = [(init, 0, [init])] # Lista de nodos a expandir guarda el nodo actual, el costo total, y el camino

    expand_count = {node: 0 for node in nodes} # Diccionario que guarda el numero de veces que se expande cada nodo

    while lista_nodos: # Mientras la lista de nodos a expandir no este vacia

        # Ordena la lista de nodos segun la funcion f(n) = g(n) + h(n) de menor a mayor
        lista_nodos.sort(key=lambda x: x[1] + nodes[x[0]])

        #Obtiene el nodo con menor costo
        node, costo, camino = lista_nodos.pop(0)

        # Si el nodo es el objetivo, retorna el camino y el costo
        if node == goal:
            return camino, costo, expand_count

        expand_count[node] += 1 # Incrementa el numero de veces que se expande el nodo

        for vecino in graph[node]: # Para cada vecino del nodo actual
            
            costo_total = costo + graph[node][vecino] # Calcula el costo que se llevaba mas el costo del vecino
            camino_nuevo = camino.copy() + [vecino] # Crea un nuevo camino con el camino actual mas el vecino
            nodo_nuevo = (vecino, costo_total, camino_nuevo) # Crea un nuevo nodo con el vecino, el costo y el camino

            lista_nodos.append(nodo_nuevo) # Agrega el nodo a la lista de nodos a expandir