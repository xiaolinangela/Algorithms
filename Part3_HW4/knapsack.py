import sys
from itertools import islice

def knapsack(nums, max_weight, total_items):
    column, row = max_weight+1, total_items+1
    table = [[0 for x in range(column)] for y in range(row)]
    for i in range(1, total_items+1):
        for j in range(0, max_weight+1):
            if j < nums[i][1] :
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(nums[i][0]+table[i-1][j-nums[i][1]], table[i-1][j])
    print(table)
    print(max(max(table)))
    return table

def main():
    if len(sys.argv) == 2:
        txt = sys.argv[1]
        with open(txt, 'r') as f:
            for line in islice(f,0,1):
                max_weight = int(line.split()[0])
                total_items = int(line.split()[1])
            nums = [[0, 0]]
            for line in islice(f,0,None):
                value = int(line.split()[0])
                weight = int(line.split()[1])
                nums.append([value, weight])
        #print(nums)
        knapsack(nums,max_weight,total_items)
    else:
        print("Error")

if __name__ == "__main__":
    main()