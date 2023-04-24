import sys
import os

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
    ultimo_nodo = 0
    for i in range(2, len(data)):
        if data[i][0].find(',') != -1:
            ultimo_nodo = i
            break
        nodes[data[i][0]] = int(data[i][1])
    
    # Crea el diccionario de aristas recorriendo la matriz
    for i in range(ultimo_nodo, len(data)):
        line = data[i] # Separa el nodo inicial y el nodo final de una arista

        for j in range(len(line)): # Elimina las comas de los nodos
            line[j] = line[j].replace(',', '')

        if line[0] in graph: # Si el nodo inicial ya esta en el diccionario de aristas
            graph[line[0]][line[1]] = int(line[2]) # Agrega el nodo final y el peso de la arista
        else: # Si el nodo inicial no esta en el diccionario de aristas
            graph[line[0]] = {line[1]: int(line[2])} # Crea el nodo inicial y agrega el nodo final y el peso de la arista

    return init,goal,nodes,graph # Retorna el nodo inicial, el nodo final, el diccionario de nodos y el diccionario de aristas
    
def read_entry():
    
    # Limpiar consola
    os.system('cls' if os.name == 'nt' else 'clear')

    #Leer entrada
    if len(sys.argv) < 2: # Si no se ingreso el nombre del archivo
        archivo = input("Ingrese el nombre del archivo: ") # Pide el nombre del archivo
    else: # Si se ingreso el nombre del archivo
        archivo = sys.argv[1] # Guarda el nombre del archivo

    if not os.path.exists(archivo): # Si el archivo no existe
        print("El archivo no existe") # Imprime un mensaje de error
        exit(1) # Sale del programa


    if len(sys.argv) < 3: # Si no se ingreso el metodo de busqueda
        print("Seleccione un metodo de busqueda")
        print("1. Busqueda en Profundidad\n2. Busqueda por Costo Uniforme\n3. Busqueda Greedy\n4. Busqueda A*")
        metodo = input("Ingrese un numero: ") # Pide el metodo de busqueda
    else: # Si se ingreso el metodo de busqueda
        metodo = sys.argv[2] # Guarda el metodo de busqueda

    os.system('cls' if os.name == 'nt' else 'clear') # Limpia la consola
    return archivo, metodo # Retorna el nombre del archivo y el metodo de busqueda