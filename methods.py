import random

def DFS(init, goal, nodes, graph):
    stack = []
    path = []
    expand_count = {node: 0 for node in nodes}
    total_cost = 0

    node = init
    stack.append(node)
    
    while stack: # Mientras el stack no este vacio (hay nodos por expandir)

        # El nodo que se elige del stack debe ser uno de los hijos del anterior
        num = random.randint(0, len(stack)-1)
        while stack[num] != init and stack[num] not in graph[node]:
            num = random.randint(0, len(stack)-1)
        
        node = stack.pop(num)
        
        if node == goal:
            path.append(node)

            # Costo total del camino
            total_cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))

            return path, total_cost, expand_count
        
        if node not in path:
            path.append(node)
            expand_count[node] += 1

            for child in graph[node]:
                stack.append(child)
    

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


# def a_estrella(init, goal, nodes, graph):
#     stack = {} # Va guardando el camino y el costo real del mismo
#     path = [init]
#     stack[path] = 0

#     print(stack)
#     expand_count = {node: 0 for node in nodes}
#     total_cost = 0


    # while True:
    #     f_min = float('inf')
    #     node_min = None

    #     for camino in stack:
            

            
def uniform_cost_search(init, goal, nodes, graph):

    



    return None




