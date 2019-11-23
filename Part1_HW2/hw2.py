from sys import argv
import math
import sys
# set a global counter
inv_count = 0
def inversions(numbers):
    # establish the base case
    global inv_count
    if len(numbers) == 2:
        new_numbers = []
        if numbers[0] < numbers[1]:
            new_numbers.append(numbers[0])
            new_numbers.append(numbers[1])
            return new_numbers
        elif numbers[0] > numbers[1]:
            new_numbers.append(numbers[1])
            new_numbers.append(numbers[0])
            # count inversions
            inv_count += 1
            return new_numbers
    elif len(numbers) == 1:
        new_numbers = []
        new_numbers.append(numbers[0])
        return new_numbers

    else:
        first_half = inversions(numbers[0:math.ceil(len(numbers) / 2)])
        second_half = inversions(numbers[math.ceil(len(numbers) / 2):])
        i = j = k = 0
        results = [0] * len(numbers)
        # merge two arrays 
        while i < len(first_half) and j < len(second_half):
            if first_half[i] < second_half[j]:
                results[k] = first_half[i]
                i += 1
            elif first_half[i] > second_half[j]:
            	# count the split inversions 
                inv_count = inv_count + len(first_half) - i
                results[k] = second_half[j]
                j += 1
            k += 1
        while i < len(first_half):
            results[k] = first_half[i]
            i += 1
            k += 1
        while j < len(second_half):
            results[k] = second_half[j]
            j += 1
            k += 1
    return results


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
        # call the inversion function
        inversions(numbers)
        print(inv_count)
    else:
        print("Error: Add a file")


if __name__ == "__main__":
    main()
