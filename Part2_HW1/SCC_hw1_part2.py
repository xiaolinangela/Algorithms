import sys, threading 
# sys.setrecursion(800000)
threading.stack_size(67108864)

def build_graph(filename):
	graph = dict()
	with open (filename, 'r') as file:
		for line in file:
			s, t = line.split()
			s, t = int(s), int(t)
			dest_nodes = graph.get(s, set())
			dest_nodes.add(t)
			graph[s] = dest_nodes
	return graph

def build_graph_rev(filename):
	graph = dict()
	with open (filename, 'r') as file:
		for line in file:
			s, t = line.split()
			s, t = int(s), int(t)
			dest_nodes = graph.get(t, set())
			dest_nodes.add(s)
			graph[t] = dest_nodes
	return graph


def SCC(graph, graph_rev):

	explored_nodes_rev = None
	explored_nodes=None
	stack = []
	# for finishing times in 1st pass
	t = 0 
	#for leaders in 2nd pass
	leaders = {}

	def toposort(graph_rev, v):
		nonlocal explored_nodes_rev
		explored_nodes_rev.add(v)
		for i in graph_rev[v]:
			if i not in explored_nodes_rev:
				toposort(graph_rev, i)
		stack.insert(0,v)

	def toposort_loop(graph_rev): 
		nonlocal explored_nodes_rev, stack
		print(graph_rev.key)
		total_nodes = len(graph_rev)
		for i in range(1,total_nodes+1):
			if i not in explored_nodes_rev:
				explored_nodes.add(i)
				toposort(graph_rev, i)

	def DFS(graph, v):
		nonlocal explored_nodes, t, leaders
		explored_nodes.add(v)
		for i in graph[v]:
			if i not in explored_nodes:
				dest_nodes = leaders.get(v, set())
				dest_nodes.add(i)
				leaders[v] = dest_nodes
				DFS(graph,i)

	def DFS_loop(graph):
		nonlocal explored_nodes, t, leaders
		for i in stack: 
			if i not in explored_nodes:
				DFS(graph,i)

	toposort_loop(graph_rev)
	DFS_loop(graph)
	return list(leaders.values())

def main():
	if len(sys.argv) == 2:
		txt_file = sys.argv[1];
		graph = build_graph(txt_file)
		graph_rev = build_graph_rev(txt_file)
		print(graph_rev)
		print(len(graph_rev))
		SCC(graph, graph_rev)
		print(leaders.values())
	else:
		print("Error: Add a file")


if __name__ == "__main__":
    main()


#thread = threading.Thread(target=main)
#thread.start()