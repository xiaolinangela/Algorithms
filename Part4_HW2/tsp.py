import sys
import matplotlib
matplotlib.use('GTK3Cairo')
import matplotlib.pyplot as plt
from itertools import islice
import numpy as np
from itertools import combinations
from itertools import chain
import time

start_time = time.time()
def tsp(distance, total_cities):
    #generate S. if a =[0,1,2], combo will generate: (),(0,),(1,),(2,),(0,1),(0,2),(1,2),(0,1,2)
    a = [i for i in range(0,total_cities)]
    combo = chain.from_iterable(combinations(a, i) for i in range(len(a)+1))
    set = [i for i in combo if 0 in i]
    A = {}
    for s in set:
        if s == (0,):
            A[s,0] = 0
        else:
            A[s,0] = 100000000000
    new_set = [i for i in set if i != (0,)]
    #generate the matrix A
    for s in new_set:
        for j in s:
            if j is not 0:
                list_s = list(s)
                list_s.remove(j)
                s_minus_j = tuple(list_s)
                cost = []
                for k in s:
                    if k != j:
                        cost.append(A[s_minus_j,k] + distance[k,j])
                A[s,j] = min(cost)
    #Calculate the shortest path back to the origin 0
    final_set = new_set[len(new_set)-1]
    final_cost = []
    for j in range(1, total_cities):
        final_cost.append(A[final_set, j] + distance[j,0])
    min_cost = int(min(final_cost))
    print(min_cost)
    return min_cost

def main():
    if len(sys.argv) == 2:
        txt = sys.argv[1]
        d = []
        with open(txt, 'r') as f:
            for line in islice(f,0,1):
                total_cities = int(line.split()[0])
            for line in islice(f,0,None):
                d.append([float(line.split()[0]), float(line.split()[1])])
        D = {} #distance hash table
        for i in range(0,total_cities):
            D[i,i] = 0
            for j in range(i+1, total_cities):
                D[i,j] = np.sqrt((d[i][0]-d[j][0])**2 + (d[i][1]-d[j][1])**2)
                D[j,i] = D[i,j]
        #print
        #divide the vertices into two sets, 0-12 and 11-24. Subtract 2*distance(11,12) from the sum in the end.
        tsp(D, total_cities)
        # n = list(range(1,26))
        # fig, ax = plt.subplots()
        # ax.scatter(x, y)
        # for i, txt in enumerate(n):
        #     ax.annotate(txt, (x[i], y[i]))
        # plt.show()
        # print(plt)
        # plt.savefig('figure1.png')
    else:
        print("Error")
if __name__ == "__main__":
    main()

print("--- %s seconds ---" % (time.time() - start_time))