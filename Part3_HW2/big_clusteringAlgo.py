import sys
from collections import OrderedDict
from operator import itemgetter
import collections
from networkx.utils.union_find import UnionFind
from itertools import combinations
import time
start_time = time.time()


def main():
	if len(sys.argv) == 2:
		txt = sys.argv[1]
		graph = {}
		total_nodes = []
		total_bits = []
		node_position = 1 
		clusters = []
		with open(txt, 'r') as file:
			for line in file:
				if len(line.split()) == 2:
					#total_nodes.append(int(line.split()[0]))
					total_bits.append(int(line.split()[1]))
				else:
					if int("".join(line.split()),2) in graph:
						clusters.remove(graph[int("".join(line.split()),2)])
					graph[int("".join(line.split()),2)] = node_position
					clusters.append(node_position)
					node_position += 1
		bits = total_bits[0]
		#print(clusters)
		#print(len(graph))
		#print(graph)
		bit_mask_1 = [1 << i for i in range(bits)]
		#print(bit_mask_1)
		bit_mask_2 = []
		for combo in combinations(range(bits),2):
			bit_mask_2.append(bit_mask_1[combo[0]]^bit_mask_1[combo[1]])
		#for i in bit_mask_2:
			#print(bin(i))
		#zero_mask = [0b000000000000000000000000]
		#print(len(bit_mask_2))
		bit_mask = bit_mask_1 + bit_mask_2
		#print(len(bit_mask))
		my_set = set(clusters)
		#print(my_set)
		u_find = UnionFind(my_set)
		#print(bit_mask)
		for bitmask in bit_mask:
			for key1 in graph:
				key2 = key1 ^ bitmask
				#print(bin(key2))
				if key2 in graph:
					#print(bin(key2))
					if u_find[graph[key1]] != u_find[graph[key2]]:
						u_find.union(graph[key1],graph[key2])
		result = list(map(sorted, u_find.to_sets()))
		print(len(result))




if __name__ == "__main__":
	main()

print("--- %s seconds ---" % (time.time() - start_time))