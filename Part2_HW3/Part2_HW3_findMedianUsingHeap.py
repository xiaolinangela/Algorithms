#python code to find median using heap data structure 

import heapq
import sys
def convertsign(numbers):
	new_numbers = []
	new_numbers[:] = [-1*x for x in numbers]
	heapq.heapify(new_numbers)
	return new_numbers

def medianheap(numbers):
	#find medians using heap
	medians = []
	heap1 = []
	heap2 = []
	for number in numbers:
		if len(heap1) == 0 :
		#push the first number in the list to heap1  
			heapq.heappush(heap1, number)
			medians.append(number)
			#print(heap1)
		else: 
			heap1_neg = convertsign(heap1)
			if number > (heap1_neg[0]*-1):
				#Add number to heap2 if number is bigger than heap1 max
				heapq.heappush(heap2, number)
				if (len(heap2)-len(heap1)) > 1:
					#balance heap1 and heap2 
					heap2_min = heapq.heappop(heap2)
					heapq.heappush(heap1, heap2_min)
					heap1_neg = convertsign(heap1)
					medians.append(heap1_neg[0]*-1)
				elif len(heap1) == len(heap2):
					heap1_neg = convertsign(heap1)
					medians.append(heap1_neg[0]*-1)
				elif (len(heap2) - len(heap1)) == 1:
					medians.append(heap2[0])

			else:
				#add number to heap1 otherwise
				heapq.heappush(heap1, number)
				heap1_neg = convertsign(heap1)
				if (len(heap1) - len(heap2)) > 1:
					#balance heap1 and heap2
					heap1_max = (heapq.heappop(heap1_neg))* -1 
					heapq.heappush(heap2, heap1_max)
					heap1 = convertsign(heap1_neg)
					medians.append(heap1_neg[0]*-1)
				elif len(heap1) == len(heap2):
					heap1_neg = convertsign(heap1)
					medians.append(heap1_neg[0]*-1)
				elif (len(heap1) - len(heap2)) == 1:
					heap1_neg = convertsign(heap1)
					medians.append(heap1_neg[0]*-1)
	#print(heap1)
	#print(heap2)
	#print(medians)
	sum_medians = sum(medians) % 10000
	return print(sum_medians)

def main(): 
	if len(sys.argv) == 2:
		text_file = sys.argv[1]
		numbers = []
		with open(text_file, 'r') as file:
			for line in file: 
				numbers.append(int(line.rstrip("\n")))
		#print(numbers)
		medianheap(numbers)
		#print(sum_medians)
	else:
		print("Error")

if __name__=="__main__":
	main()
