
import sys
import random
import time



def selectionSort(arr):
    arrayLen = len(arr)
    for outerIndex in range(arrayLen):
    
        
        minIndex = outerIndex
        for innerIndex in range(outerIndex + 1, arrayLen):
            if arr[minIndex] > arr[innerIndex]:
                minIndex = innerIndex
    
    
        arr[outerIndex], arr[minIndex] = arr[minIndex], arr[outerIndex]
    return arr




file = open("SelectionSort.csv","a")
for _ in range(10):
    input = [0 for i in range(10000)]
    for i in range(10000):
        input[i] = random.randint(1, 10000)


    start = int(time.time()*1000)
    output = selectionSort(input)
    print (output)
    end = int(time.time()*1000)
    total=end-start
    file.write(str(total) + ", ")

file.write("\n")