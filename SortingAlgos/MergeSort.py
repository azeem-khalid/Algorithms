import math
import random
import time
import csv

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] *(n1)
    R = [0] *(n2)

    for i in range(0, n1):
        L[i] = arr[left + i]

    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = math.floor((l + (r - 1)) // 2)
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


arr = [0] * 10000

for i in range(len(arr)):
    arr[i]=random.randint(0,100000)



n = len(arr)

timeArr= [0]*10

for i in range(len(timeArr)):
    start_time = time.time()*1000
    mergeSort(arr, 0, n - 1)
    endtime= time.time()*1000
    timeArr[i]=endtime-start_time



myData= [['Merge Sort Execution Time',timeArr[0],timeArr[1],timeArr[2],timeArr[3],timeArr[4],timeArr[5],timeArr[6],timeArr[7],timeArr[8],timeArr[9]]]
myFile = open('mergesort.csv', 'a')
with myFile:
   writer = csv.writer(myFile)
   writer.writerows(myData)
