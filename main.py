import graph as g
import methods as m

def main():
    data = g.load_graph('graph.txt')
    init,goal,nodes,graph = g.create_graph(data)
    
    print(m.DFS(init, goal, nodes, graph))
    # print(m.DFS(init, goal, nodes, graph))

if __name__ == "__main__":
    main()




