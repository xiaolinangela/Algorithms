#use greedy algorithm diff to minimizing the weighted sum of completion times
import sys
import itertools 
import collections
from operator import itemgetter

def main():
	if len(sys.argv) ==2:
		txt = sys.argv[1]
		#print("hello")
		job = []
		with open(txt, 'r') as file:
			for line in itertools.islice(file,1,None):
				weight = int(line.split()[0])
				length = int(line.split()[1])
				job.append([weight, length, weight-length])
		#print(job)
		sorted_job = sorted(job, key=itemgetter(2,1),reverse=True)
		#print(sorted_job)
		ct = 0
		total_length = 0
		for item in sorted_job: 
			total_length = total_length + item[1]
			ct = ct + (item[0] * total_length)
		print(ct)

if __name__ == "__main__" :
	main()


