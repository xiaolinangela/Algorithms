import sys
from itertools import islice
import heapq

def dijkstra(graph, source, total_nodes):
    nodes = [] #priority queue of all nodes in graph
    distance = {} #distance from start to node
    previous = dict() #previous node
    #print(graph)
    for i in range(1, total_nodes+1):
        if i == source:
            distance[i] = 0  #set the source vertex distance to be zero
            heapq.heappush(nodes, [distance[i], i]) #store the distance with vertex key in heap
        else:
            distance[i] = sys.maxsize #set all the other vertext distance as infinity
            heapq.heappush(nodes, [distance[i], i])
    #print(nodes)
    previous[i] = None
    #print(distance)
    while nodes:
        u = heapq.heappop(nodes)[1] #vertex in nodes with the smallest distance
        if u == source:
            previous[u] = None
        if u not in graph:
            continue
        else:
            for neighbor in graph[u]:
                alt = distance[u] + graph[u][neighbor]
                # if the new distance is smaller than the existing distance, existing distance become the smaller distance
                if alt < distance[neighbor]:
                    #print(neighbor)
                    distance[neighbor] = alt
                    previous[neighbor] = u
                    for n in nodes:
                        #reassign the distance value in nodes heap structure
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes) #re-heapify the nodes
    #print(distance)
    del distance[source]
    return distance


def johnsons(graph, total_nodes):
    #add a new vertex s & a new edge (s,v) with length 0 for each v in G
    for i in range(1,total_nodes+1):
        s = 0
        values = graph.get(s, dict())
        values.update({i:0})
        graph[s] = values
    # Run Bellman-Ford on G' with source
    distance = {}
    parents = {}
    for i in range(0, total_nodes+2):
        distance[i] = float('Inf')
        parents[i] = None
    distance[s] = 0 #source distance is zero
    for i in range(total_nodes):
        for u in graph:
            for v in graph[u]:
                if distance[v] > distance[u] + graph[u][v]:
                    distance[v] = distance[u] + graph[u][v]
                    parents[v] = u
    for u in graph:
        for v in graph[u]:
            if distance[v] > distance[u] + graph[u][v]:
                return print("Graph has negative weight cycles")

    #Reassign the edge cost Ce' = Ce + Pu - Pv
    for u in graph:
        for v in graph[u]:
            graph[u][v] = graph[u][v] + distance[u] - distance[v]
    del graph[s]
    #Run Dijkstra on each vertex
    # del graph[s]  #remove the added source vertex
    sd = {}
    for u in graph:
        #print(a)
        sd[u] = dijkstra(graph,u,total_nodes)
    #Readjust the distance from re-weighting
    for u in sd:
        for v in sd[u]:
            sd[u][v] = sd[u][v] - distance[u] + distance[v]
    result = []
    for u in sd:
        for v in sd[u]:
            result.append(sd[u][v])
    print(min(result))
    return sd


def main():
    if len(sys.argv) == 2:
        txt = sys.argv[1]
        graph = dict()
        with open(txt, 'r') as f:
            for line in islice(f,0,1):
                total_nodes = int(line.split()[0])
                total_edges = int(line.split()[1])
            for line in islice(f,0,None):
                tail_node = int(line.split()[0])
                head_node = int(line.split()[1])
                edge_cost = int(line.split()[2])
                dest_node = graph.get(tail_node, dict())
                dest_node.update({head_node : edge_cost})
                graph[tail_node] = dest_node
        johnsons(graph, total_nodes)
    else:
        print("error")

if __name__ == "__main__":
    main()