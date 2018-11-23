import sys
import random
import time



def swap(arr,i,j):
    arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubbleSort(arr):
    n = len(arr)


    for i in range(n):


        for j in range(0, n - i - 1):


            if arr[j] > arr[j + 1]:
                swap(arr,i,j)


file = open("BubbleSort.csv","a")
for _ in range(1):
    input = [0 for i in range(10000)]
    for i in range(10000):
        input[i] = random.randint(1, 10000)

    n = len(input)
    startBubble = int(time.time()*1000)
    bubbleSort(input)
    endBubble = int(time.time()*1000)
    print(input)
    total=endBubble-startBubble
    file.write(str(total) + ", ")

file.write("\n")
