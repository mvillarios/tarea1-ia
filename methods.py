import random

# def DFS(init, goal, nodes, graph):
#     stack = []
#     path = []
#     expand_count = {node: 0 for node in nodes}
#     total_cost = 0

#     node = init
#     stack.append(node)
    
#     while stack: # Mientras el stack no este vacio (hay nodos por expandir)

#         # El nodo que se elige del stack debe ser uno de los hijos del anterior
#         num = random.randint(0, len(stack)-1)
#         while stack[num] != init and stack[num] not in graph[node]:
#             num = random.randint(0, len(stack)-1)
        
#         node = stack.pop(num)
        
#         if node == goal:
#             path.append(node)

#             # Costo total del camino
#             total_cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))

#             return path, total_cost, expand_count
        
#         if node not in path:
#             path.append(node)
#             expand_count[node] += 1

#             for child in graph[node]:
#                 stack.append(child)
    

# def a_estrella(init, goal, nodes, graph):
#     stack = [init]
#     path = []
#     expand_count = {node: 0 for node in nodes}
#     total_cost = 0

#     while stack:
#         f_min = float('inf')
#         node_min = None
#         print("Stack: ",stack)
#         print("Path: ",path)
#         for node in stack: 
#             if node != init and node in graph[path[-1]]:
#                 g = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1)) + graph[path[-1]][node]
#             elif node != init and node not in graph[path[-1]]:
#                 continue
#             else:
#                 g = 0
#             h = nodes[node]
#             f = g + h
#             if f < f_min:
#                 f_min = f
#                 node_min = node

#         if node_min == goal:
#             path.append(node_min)
#             total_cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
#             return path, total_cost, expand_count

#         stack.remove(node_min)
#         if node_min not in path:
#             path.append(node_min)
#             expand_count[node_min] += 1

#             for child in graph[node_min]:
#                 stack.append(child)



            

            
def uniform_cost_search(init, goal, nodes, graph):

    lista_nodos = [(init, 0, [init])] # Lista de nodos a expandir guarda el nodo actual, el costo total, y el camino

    expand_count = {node: 0 for node in nodes}

    while lista_nodos:

        # Ordena la lista de nodos por costo
        lista_nodos.sort(key=lambda x: x[1])

        # Obtiene el nodo con menor costo
        node, costo, camino = lista_nodos.pop(0)

        # Si el nodo es el objetivo, retorna el camino y el costo
        if node == goal:
            return camino, costo, expand_count


        expand_count[node] += 1
        for vecino in graph[node]:
            
            costo_total = costo + graph[node][vecino]
            camino_nuevo = camino.copy() + [vecino]
            nodo_nuevo = (vecino, costo_total, camino_nuevo)

            lista_nodos.append(nodo_nuevo)


    return None


def a_estrella(init, goal, nodes, graph):
    lista_nodos = [(init, 0, [init])] # Lista de nodos a expandir guarda el nodo actual, el costo total, y el camino

    expand_count = {node: 0 for node in nodes}

    #count = 0
    while lista_nodos:

        # Ordena la lista de nodos segun la funcion f(n) = g(n) + h(n) de menor a mayor
        lista_nodos.sort(key=lambda x: x[1] + nodes[x[0]])
        #count += 1
        #print("Iteracion: ",count)
        # for nodo in lista_nodos:
        #     print("Camino: ",nodo[2], " Costo: ",nodo[1] + nodes[nodo[0]])
        # Obtiene el nodo con menor costo
        node, costo, camino = lista_nodos.pop(0)
        
        #print("Camino tomado: ", camino)

        # Si el nodo es el objetivo, retorna el camino y el costo
        if node == goal:
            return camino, costo, expand_count

        expand_count[node] += 1 

        for vecino in graph[node]:
            
            costo_total = costo + graph[node][vecino]
            camino_nuevo = camino.copy() + [vecino]
            nodo_nuevo = (vecino, costo_total, camino_nuevo)

            lista_nodos.append(nodo_nuevo)

        

    return None


def DFS(init, goal, nodes, graph):
    
    lista_nodos = [(init, 0, [init])] 

    expand_count = {node: 0 for node in nodes}

    visited = set()

    while lista_nodos:

        node, costo, camino = lista_nodos.pop(random.randint(0, len(lista_nodos)-1))

        if node == goal:
            return camino, costo, expand_count

        visited.add(node)

        for vecino in graph[node]:
            if vecino not in visited:
                costo_total = costo + graph[node][vecino]
                camino_nuevo = camino.copy() + [vecino]
                nodo_nuevo = (vecino, costo_total, camino_nuevo)
                lista_nodos.append(nodo_nuevo)
                

def greedy(init, goal, nodes, graph):

    lista_nodos = [(init, 0, [init])] # Lista de nodos a expandir guarda el nodo actual, el costo total, y el camino

    expand_count = {node: 0 for node in nodes}

    while lista_nodos:

        # Ordena la lista de nodos por costo
        lista_nodos.sort(key=lambda x: nodes[x[0]])

        # Obtiene el nodo con menor costo
        node, costo, camino = lista_nodos.pop(0)

        # Si el nodo es el objetivo, retorna el camino y el costo
        if node == goal:
            return camino, costo, expand_count


        expand_count[node] += 1
        for vecino in graph[node]:
            
            costo_total = costo + graph[node][vecino]
            camino_nuevo = camino.copy() + [vecino]
            nodo_nuevo = (vecino, costo_total, camino_nuevo)

            lista_nodos.append(nodo_nuevo)