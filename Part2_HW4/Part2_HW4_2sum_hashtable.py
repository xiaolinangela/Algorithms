#using hash table to solve 2 sum problems
import sys
import bisect
import time
start_time = time.time()
def main():
	if len(sys.argv) == 2:
		text_file = sys.argv[1]
		numbers = []
		with open(text_file, 'r') as file:
			for line in file:
				numbers.append(int(line.rstrip("\n")))
		#htable = {}
		numbers.sort()
		n = len(numbers)
		concat = []
		subarray = []
		for x in numbers:
			lower_index = bisect.bisect_left(numbers, -10000-x)
			upper_index = bisect.bisect_left(numbers, 10000-x)
			subarray = numbers[lower_index:upper_index]
			mapped_subarry = [x+i for i in subarray]
			concat.extend(mapped_subarry)
		unique_concat = set(concat)
		print(len(unique_concat))

		#print(htable)
		# count = 0
		# list_y = []
		# for i in range(-10000, 10001):
		# 	for j in numbers:
		# 		y = i - j
		# 		if y in htable.values():
		# 			count = count + 1
		# 			break
		# print(count)

	else:
		print("Error")


if __name__ =="__main__":
	main()

print("--- %s seconds ---" % (time.time() - start_time))

