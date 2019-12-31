import sys 
import heapq
import itertools 
import random
import time
start_time = time.time()
def prim(graph, graph_info):
	num_vertices = graph_info[0]
	num_edges = graph_info[1]
	vertices = [] #a heap structure
	key = {} #store the edge_cost 
	source = random.randint(1,num_vertices) #randomly choose a source
	Tree = []
	introduced = {} #vertex with edges that introduced to its minimum edge cost 
	unexplored = list(range(1,num_vertices+1)) #keep track of unexplored vertex
	for vertex in range(1, num_vertices+1): #initialze all the vertex edge cost to inifinity, except the source = 0, & store the data in a heap structure 
		if vertex == source:
			key[vertex] = 0
			heapq.heappush(vertices, [key[vertex], vertex])
		else:
			key[vertex] = sys.maxsize
			heapq.heappush(vertices, [key[vertex], vertex])
	#print(vertices)
	while vertices: #until vertices is empty 
		w = heapq.heappop(vertices)[1] #remove the minimum edge cost from the heap structure, and store the vertext as w
		unexplored.remove(w) 
		if w == source: 
			introduced[w] = None
		else: 
			Tree.append(introduced[w])
		#explore w's neighbor and update neighbor's edge cost if w-neighbor edge cost is lower
		for neighbor in graph[w]:
			if neighbor in unexplored: 
				for vertex in vertices:
					if vertex[1] == neighbor and graph[w][neighbor] < vertex[0]:
						vertex[0] = graph[w][neighbor]
						introduced[neighbor] = w, neighbor #update vertex's edge 
			heapq.heapify(vertices)

		#print(vertices)
	total_cost = 0
	for i in Tree:
		total_cost += graph[i[0]][i[1]]
	#print(Tree)
	#print(total_cost)
	return total_cost

def main():
	if len(sys.argv) == 2:
		txt = sys.argv[1]
		graph = {}
		graph_info = []
		with open(txt, 'r') as file:
			for line in file:
				if len(line.split()) == 2:
					total_vertex = int(line.split()[0])
					total_edge = int(line.split()[1])
					graph_info.append(total_vertex)
					graph_info.append(total_edge)
				else: 
					edge1 = int(line.split()[0])
					edge2 = int(line.split()[1])
					edge_cost = int(line.split()[2])
					dest_node = graph.get(edge1, dict())
					dest_node.update({edge2:edge_cost})
					graph[edge1] = dest_node
					dest_node_2 = graph.get(edge2,dict())
					dest_node_2.update({edge1:edge_cost})
					graph[edge2] = dest_node_2
		#print(graph)
		#print(graph_info)
		print(prim(graph,graph_info))
	else: 
		print("Error")

if __name__ == "__main__":
	main()

print("--- %s seconds ---" % (time.time() - start_time))