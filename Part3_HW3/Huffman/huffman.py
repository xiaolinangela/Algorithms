import sys
from itertools import islice
from operator import itemgetter
import heapq

class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)
	def print_tree(self, traversal_type):
		if traversal_type == "pre_order":
			return self.pre_order_print(self.root, "")
	def pre_order_print(self, start, traversal):
		if start:
			traversal += (str(start.value) + "-")
			traversal = self.pre_order_print(start.left, traversal)
			traversal = self.pre_order_print(start.right, traversal)
		return traversal
	def max_height(self, node):
		if node is None:
			return -1
		left_height = self.max_height(node.left)
		right_height = self.max_height(node.right)
		return 1+ max(left_height, right_height)

	def min_height(self, node):
		if node is None:
			return -1
		right_height = self.min_height(node.left)
		left_height = self.min_height(node.right)
		return 1+ min(left_height, right_height)

def huffman(f, pa):
	while len(list(f.keys())) >= 2:
		removed_1 = heapq.heappop(pa)
		tree1_key = removed_1[1]
		tree1_pa = removed_1[0]
		removed_2 = heapq.heappop(pa)
		tree2_key = removed_2[1]
		tree2_pa = removed_2[0]
		new_key = tree1_pa + tree2_pa
		new_tree = BinaryTree(new_key)
		new_tree.root.left = f[tree1_key].root
		new_tree.root.right = f[tree2_key].root
		f[new_key] = new_tree
		del f[tree1_key]
		del f[tree2_key]
		new_tree_pa = tree1_pa + tree2_pa
		heapq.heappush(pa, [new_tree_pa, new_key])
	return f, pa

def main():
	if len(sys.argv) == 2:
		txt = sys.argv[1]
		pa = []
		with open(txt, 'r') as f:
			symbol = 1
			for line in islice(f,1, None):
				heapq.heappush(pa, [int(line.rstrip("/n")), symbol])
				symbol = symbol + 1
		f = {}
		for i in range(1,symbol):
			tree = BinaryTree(i)
			f[i] = tree
		huffman(f, pa)
		f_key = next(iter(f))
		print(f[f_key].max_height(f[f_key].root))
		print(f[f_key].min_height(f[f_key].root))

	else:
		print("error")

if __name__ == "__main__":
	main()