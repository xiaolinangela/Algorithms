import sys, threading 
sys.setrecursionlimit(800000)
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

	explored_nodes_rev = set()
	explored_nodes= set()
	stack = []
	# for finishing times in 1st pass
	t = 0 
	#for leaders in 2nd pass
	leaders = {}
	current_leader = 0

	def toposort(graph_rev, v):
		nonlocal explored_nodes_rev, stack
		explored_nodes_rev.add(v)
		#print(v)
		if v in graph_rev:
			for i in graph_rev[v]:
				if i not in explored_nodes_rev:
					toposort(graph_rev, i)
		stack.insert(0,v)

	def toposort_loop(graph_rev): 
		nonlocal explored_nodes_rev, stack
		#total_nodes = len(graph_rev)
		#print(total_nodes)
		nodes = list(graph_rev.keys())
		#print(nodes)
		for i in nodes:
			if i not in explored_nodes_rev:
				explored_nodes_rev.add(i)
				toposort(graph_rev, i)

	def DFS(graph, v):
		nonlocal explored_nodes, t, leaders, current_leader
		explored_nodes.add(v)
		if v in graph: 
			for i in graph[v]:
				if i not in explored_nodes:
					dest_nodes = leaders.get(current_leader, set())
					dest_nodes.add(i)
					leaders[current_leader] = dest_nodes
					DFS(graph,i)

	def DFS_loop(graph):
		nonlocal explored_nodes, t, leaders, current_leader
		for i in stack: 
			if i not in explored_nodes:
				explored_nodes.add(i)
				leaders[i] = set()
				current_leader = i
				DFS(graph,i)

	toposort_loop(graph_rev)
	DFS_loop(graph)
	#print(stack)
	SCC_size = []
	for key in leaders:
		SCC_size.append(len(leaders[key])+1)
	result = sorted(SCC_size)
	result.reverse()
	print(result[0:5])
	#print(leaders)
	return leaders

def main():
	if len(sys.argv) == 2:
		txt_file = sys.argv[1]
		#print("hello world")
		graph = build_graph(txt_file)
		#print("hello world 2")
		graph_rev = build_graph_rev(txt_file)
		#print(graph)
		#print(graph_rev)
		SCC(graph, graph_rev)
		#print(leaders)
	else:
		print("Error: Add a file")


#if __name__ == "__main__":
thread = threading.Thread(target=main)
thread.start()


