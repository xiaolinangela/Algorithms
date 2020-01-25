import sys
import heapq

def dijkstra(graph, source, total_nodes):
    nodes = []; #priority queue of all nodes in graph
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
        #print(nodes)
        #print(distance)
        if u == source:
            previous[u] = None
        #print(u)
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
    # all_distance = []
    # for u in distance:
    #     all_distance.append(distance[u])
    print(distance[197])
    return distance
def main():
	if len(sys.argv) == 2:
		text_file = sys.argv[1]
		graph = dict()
		edges = dict()
		with open(text_file, 'r') as file:
			for line in file:
				txt = line.split()
				vertex = txt[0]
				for item in txt:
					if item is not vertex:
						s, t = item.split(',')
						dest_node = graph.get(int(vertex), dict())
						dest_node.update({int(s):int(t)})
						graph[int(vertex)] = dest_node
		#print(graph[200])
		dijkstra(graph, 1, 200)
	else:
		print("Error")

if __name__=="__main__":
	main()
