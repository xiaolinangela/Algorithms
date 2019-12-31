import sys
from collections import OrderedDict
from operator import itemgetter
import collections


class Cluster:
	# n is the number of nodes
	def __init__(self, nodes, sorted_graph, clustersize): 
		self.parents = [i for i in range(nodes+1)]
		self.ranks = [1 for i in range(nodes+1)]
		self.clusters = []
		for i in range(1, nodes+1):
			self.clusters.append([i])
		self.graph = {}
		self.graph = sorted_graph 
		self.clustersize = clustersize
		self.nodes = nodes
		self.spacing = []
	def findSet(self, node):
		if node != self.parents[node]:
			self.parents[node] = self.findSet(self.parents[node])
		return self.parents[node]

	def union(self, nodeA, nodeB):
		self.link(self.findSet(nodeA), self.findSet(nodeB))

	def link(self, nodeA, nodeB):
		if self.ranks[nodeA] > self.ranks[nodeB]:
			self.parents[nodeB] = nodeA
			self.clusters.remove([nodeB])
		else:
			self.parents[nodeA] = nodeB
			self.clusters.remove([nodeA])
			if self.ranks[nodeA] == self.ranks[nodeB]:
				self.ranks[nodeB] = self.ranks[nodeB] + 1 

	def updateParents(self):
		for i in range(1, self.nodes+1):
			if self.parents[i] not in self.clusters:
				self.parents[i] = self.findSet(self.parents[i])

	def findClusters(self): 
		for key in self.graph:
			#print(key)
			if len(self.clusters) == self.clustersize:
				#print(self.clusters)
				return self.clusters
			else:
				if self.findSet(key[0]) != self.findSet(key[1]):
					self.union(key[0],key[1])
		return self.clusters

	def findMaxSpacing(self):
		for i in range(0,self.clustersize-1):
			for j in range(1, self.nodes+1):
				if self.parents[j] == self.clusters[i][0] and j != self.clusters[i][0]:
					self.clusters[i].append(j)
		for i in range(0,self.clustersize-1):
			for j in range(0, len(self.findClusters()[i])):
				for m in range(1, self.nodes+1):
					if m not in self.findClusters()[i]:
						self.spacing.append(self.graph.get((self.findClusters()[i][j],m), sys.maxsize))
		print(min(self.spacing))
		return self.spacing

def main():
	if len(sys.argv) == 2:
		txt = sys.argv[1]
		graph = {}
		graph_info = []
		with open(txt, 'r') as file:
			for line in file:
				if len(line.split()) == 1:
					graph_info.append(int(line.split()[0]))
				else:
					edge_1 = int(line.split()[0])
					edge_2 = int(line.split()[1])
					edge_cost = int(line.split()[2])
					key = (edge_1, edge_2)
					graph[key] = edge_cost
		sorted_graph = {}
		for key, value in sorted(graph.items(), key = itemgetter(1)):
			sorted_graph[key] = value
		clustersize = 4
		result = Cluster(graph_info[0], sorted_graph,clustersize)
		#print(result.clusters)
		result.findClusters()
		result.updateParents()
		result.findMaxSpacing()
		#print(result.clusters)
		#print(result.parents)
		# for i in range(0,clustersize-1):
		# 	for j in range(1, graph_info[0]+1):
		# 		if result.parents[j] == result.clusters[i][0] and j != result.clusters[i][0]:
		# 			result.clusters[i].append(j)
		# #print(result.clusters)
		# spacing = []
		# for i in range(0,clustersize-1):
		# 	for j in range(0, len(result.clusters[i])):
		# 		for m in range(1, graph_info[0]+1):
		# 			if m not in result.clusters[i]:
		# 				#print(spacing)
		# 				spacing.append(sorted_graph.get((result.clusters[i][j],m), sys.masize))
		# print(min(result.spacing))
		#print(result.parents[2])
	else:
		print("error")

if __name__ == "__main__":
	main()