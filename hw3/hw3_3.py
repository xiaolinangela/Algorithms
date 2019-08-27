from sys import argv
import math
import sys
from statistics import median
#Use the median element as the pivot 
comparisons = 0 
def partition(numbers, left, right):
    global comparisons
    #print(numbers[left:right])
    # if len(numbers) is odd 
    if len(numbers[left:right]) % 2 != 0:
        pivot = median([numbers[left], numbers[left+len(numbers[left:right])//2], numbers[right-1]])
    else:
        pivot = median([numbers[left], numbers[left+int(len(numbers[left:right])/2-1)], numbers[right-1]])
    #print(pivot)

    if pivot == numbers[left+len(numbers[left:right])//2]:
        numbers[left], numbers[left+len(numbers[left:right])//2] = numbers[left+len(numbers[left:right])//2], numbers[left]
    elif pivot == numbers[left+len(numbers[left:right])//2-1]:
        numbers[left], numbers[left+len(numbers[left:right])//2-1] = numbers[left+len(numbers[left:right])//2-1], numbers[left]

    if pivot == numbers[right-1]:
        numbers[left], numbers[right-1] = numbers[right-1], numbers[left]
        pivot = numbers[left]
        i = left + 1
        subarray_size = len(numbers[left:right])
        comparisons = comparisons + subarray_size - 1
        for j in range(i,right):
            if numbers[j] < pivot:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                i += 1
        numbers[left], numbers[i-1] = numbers[i-1], numbers[left]
        return i-1
    else: 
        i = left + 1
        #subarray_size = len(numbers[left:right])
        #comparisons = comparisons + subarray_size - 1
        for j in range(i,right):
            comparisons +=1
            if numbers[j] < pivot:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                i += 1
        numbers[left], numbers[i-1] = numbers[i-1], numbers[left]
        return i-1

def quicksort(numbers,left,right):
    global comparisons
    if left < right:
        split = partition(numbers,left,right)
        quicksort(numbers,left,split)
        quicksort(numbers,split+1,right)
    return numbers

def main():
    if len(sys.argv) == 2:
        texts = sys.argv[1]
        numbers = []
        # read the numbers from the file and store them in a list
        with open(texts, 'r') as file:
            for line in file:
                numbers.append(line.rstrip("\n"))
        # convert strings to numbers
        numbers = [int(i) for i in numbers]
        i = numbers[0]
        # call the quicksort function
        left = 0
        right = len(numbers)
        quicksort(numbers,left,right)
        #print(numbers)
        print(comparisons)
    else:
        print("Error: Add a file")


if __name__ == "__main__":
    main()