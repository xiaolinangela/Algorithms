from sys import argv
import math
import sys
inv_count = 0
def inversions(numbers):
    # establish the base case
    global inv_count
    if len(numbers) == 2:
        new_numbers = []
        if numbers[0] < numbers[1]:
            new_numbers.append(numbers[0])
            new_numbers.append(numbers[1])
            #print(new_numbers, count)
            return new_numbers, inv_count
        elif numbers[0] > numbers[1]:
            new_numbers.append(numbers[1])
            new_numbers.append(numbers[0])
            inv_count += 1
            #print(inv_count)
            return new_numbers, inv_count
    elif len(numbers) == 1:
        new_numbers = []
        new_numbers.append(numbers[0])
        return new_numbers, inv_count

    else:
        first_half = inversions(numbers[0:math.ceil(len(numbers) / 2)])[0]
        second_half = inversions(numbers[math.ceil(len(numbers) / 2):])[0]
        i = j = k = 0
        results = [0] * len(numbers)
        while i < len(first_half) and j < len(second_half):
            if first_half[i] < second_half[j]:
                results[k] = first_half[i]
                i += 1
            elif first_half[i] > second_half[j]:
                inv_count = inv_count + len(first_half) - i
                results[k] = second_half[j]
                j += 1
                #print(inv_count)
            k += 1
        while i < len(first_half):
            results[k] = first_half[i]
            i += 1
            k += 1
        while j < len(second_half):
            results[k] = second_half[j]
            j += 1
            k += 1
        #print(results)
    return results, inv_count


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
        # print(numbers)
        i = numbers[0]
        # print(type(i))
        # call the inversion function
        inversions(numbers)
        print(inv_count)
    else:
        print("Error: Add a file")


if __name__ == "__main__":
    main()
