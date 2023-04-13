import random

def DFS(init, goal, nodes, graph):
    stack = []
    expand_count = {node: 0 for node in nodes} 
    path = []
    total_cost = 0

    node = init
    stack.append(node)

    first = True
    
    while stack:

        # El nodo que se elige del stack debe ser uno de los hijos del anterior
        num = random.randint(0, len(stack)-1)
        while first == False and stack[num] not in graph[node]:
            num = random.randint(0, len(stack)-1)
        
        first = False
        node = stack.pop(num)
        
        if node == goal:
            path.append(node)
            # Costo total del camino
            for i in range(len(path)-1):
                total_cost += graph[path[i]][path[i+1]]

            return path, total_cost, expand_count
        
        if node not in path:
            path.append(node)
            expand_count[node] += 1

            # Si el nodo no tiene hijos, se revisan los nodos anteriores
            if node not in graph:
                path.pop()
            # Si el nodo tiene hijos, se agrega el hijo al stack
            else:
                for child in graph[node]:
                    stack.append(child)

        

    for i in range(len(path)-1):
        total_cost += graph[path[i]][path[i+1]]
    return path, total_cost, expand_count



