import time
import random
import csv

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [0] * 10000

timeArr= [0]*10

for i in range(len(timeArr)):
    start_time = time.time()*1000
    for j in range(10000):
        arr[j] = random.randint(0, 10000)
    insertionSort(arr)
    endtime= time.time()*1000
    timeArr[i]=endtime-start_time


myData= [['Insertion Sort Execution Time',timeArr[0],timeArr[1],timeArr[2],timeArr[3],timeArr[4],timeArr[5],timeArr[6],timeArr[7],timeArr[8],timeArr[9]]]
myFile = open('insort.csv', 'a')
with myFile:
   writer = csv.writer(myFile)
   writer.writerows(myData)
