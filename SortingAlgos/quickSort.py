import sys
import random
import time



def swap(arr ,i , j):
    arr[i], arr[j] = arr[j], arr[i]

def createPartition(arr, lowerIndex, upperIndex):
    i = (lowerIndex - 1)
    pivot = arr[upperIndex]

    for j in range(lowerIndex, upperIndex):


        if arr[j] <= pivot:

            i = i + 1
            swap(arr,i,j)

    arr[i + 1], arr[upperIndex] = arr[upperIndex], arr[i + 1]
    return (i + 1)



def quickSort(arr, lowerIndex, upperIndex):
    if lowerIndex < upperIndex:

        pi = createPartition(arr, lowerIndex, upperIndex)


        quickSort(arr, lowerIndex, pi - 1)
        quickSort(arr, pi + 1, upperIndex)




file = open("QuickSort.csv","a")
for _ in range(10):
    input = [0 for i in range(10000)]
    for i in range(10000):
        input[i] = random.randint(1, 10000)




    n = len(input)
    start = int(time.time() * 1000)
    quickSort(input, 0, n - 1)
    print (input)
    end = int(time.time()*1000)
    total=endRadix-startRadix
    file.write(str(total) + ", ")

file.write("\n")