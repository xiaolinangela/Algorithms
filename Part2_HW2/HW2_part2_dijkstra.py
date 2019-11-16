#Python code to cacalute the shortest path between two nodes in a graph

#import "heapq" to implement heap queue
import heapq 
import sys

def dijkstra(graph, source, finish):
	nodes = []; #priority queue of all nodes in graph
	distance = {} #distance from start to node
	previous = dict() #previous node

	for vertex in graph:
		if vertex == source: 
			distance[vertex] = 0  #set the source vertex distance to be zero
			heapq.heappush(nodes, [distance[vertex], vertex]) #store the distance with vertex key in heap
		else:
			distance[vertex] = sys.maxsize #set all the other vertext distance as infinity
			heapq.heappush(nodes, [distance[vertex], vertex])
	previous[vertex] = None 

	while nodes: 
		u = heapq.heappop(nodes)[1] #vertex in nodes with the smallest distance 
		if u == source:
			previous[u] = None
		else: 
			if u == finish: 
				path =[]
				while previous[u]:
					path.append(u)
					u = previous[u]
				return print(path)

		for neighbor in graph[u]: #explore neighbor of the smallest distance 
			alt = distance[u] + graph[u][neighbor] 
			if alt < distance[neighbor]: #if the new distance is smaller than the existing distance, existing distance become the smaller distance 
				distance[neighbor] = alt 
				previous[neighbor] = u 
				for n in nodes: #reassign the distance value in nodes heap structure 
					if n[1] == neighbor:
						n[0] = alt
						break
				heapq.heapify(nodes) #re-heapify the nodes 
		#print(removed) 
	#print(distance[7])
	#print(distance[37])	
	#print(distance[59])	
	#print(distance[82])	
	#print(distance[99])	
	#print(distance[115])	
	#print(distance[133])
	#print(distance[165])	
	#print(distance[188])
	#print(distance[197])
	#print(previous[200])			
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


