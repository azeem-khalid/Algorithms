import sys
from collections import defaultdict
import os
import random
import time
def insertion(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key


def merge(array,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = [0 for i in range(n1+1)]
    R = [0 for j in range(n2+1)]

    for i in range(0,n1):
        L[i] = array[p+i]

    for j in range(0,n2):
        R[j] = array[q+j+1]

    i=0
    j=0
    k=p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i+=1
        else:
            array[k] = R[j]
            j+=1
        k+=1

    while i < n1:
        array[k] = L[i]
        i+=1
        k+=1

    while j < n2:
        array[k] = R[j]
        j+=1
        k+=1

def mergeSort(arr,p,r):
    if p < r:
        q = (p+r)//2
        mergeSort(arr,p,q)
        mergeSort(arr,q+1,r)
        merge(arr,p,q,r)


def bubble(mylist):
    for i in range(len(mylist)-1,0,-1):
        for j in range(i):
            if mylist[j] > mylist[j+1]:
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp


def selection(mylist):
    for i in range(len(mylist)-1,0,-1):
        maxPosition=0
        for j in range(1,i+1):
            if mylist[j] > mylist[maxPosition]:
                maxPosition = j
        temp = mylist[i]
        mylist[i] = mylist[maxPosition]
        mylist[maxPosition] = temp


def countSort(array):
    maxval = max(array)
    n = len(array)
    m = maxval + 1
    count = [0] * m               
    for a in array:
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]): 
            array[i] = a
            i += 1
    return array 


def countingSort(arr, exp1):
 
    n = len(arr)
     output = [0] * (n)
 
    count = [0] * (10)

    for i in range(0, n):
        index = (arr[i]//exp1)
        count[ (index)%10 ] += 1
 
    for i in range(1,10):
        count[i] += count[i-1]
 
    i = n-1
    while i>=0:
        index = (arr[i]//exp1)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1

    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]
 

def radix(arr):
 

    max1 = max(arr)
 

    exp = 1
    while max1//exp > 0:
        countingSort(arr,exp)
        exp *= 10








def main():
    

    	
        file = open("Project.txt","a")
        for i in range(10):
            array = [0 for i in range(10000)]
            for i in range(10000):
                array[i] = random.randint(1,10000)
            #time for bubble sort
            start1 = int(time.time()*1000)
            bubble(array)
            end1 = int(time.time()*1000)
            total1= end1 - start1
            #time for Selection sort
            for i in range(10000):
                array[i] = random.randint(1,10000)
            start2= int(time.time()*1000)
            selection(array)
            end2= int(time.time()*1000)
            total2= end2- start2
            #time for insertion sort
            for i in range(10000):
                array[i] = random.randint(1,10000)
            start3= int(time.time()*1000)
            insertion(array)
            end3= int(time.time()*1000)
            total3= end3- start3
            #time for Merge sort
            for i in range(10000):
                array[i] = random.randint(1,10000)
            start4= int(time.time()*1000)
            mergeSort(array,0,len(array)-1)
            end4= int(time.time()*1000)
            total4 = end4 - start4
            #time for Counting sort
            for i in range(10000):
                array[i] = random.randint(1,10000)
            start5= int(time.time()*1000)
            array = countSort(array)
            end5= int(time.time()*1000)
            total5 = end5 - start5
            #time for Radix sort
            for i in range(10000):
                array[i] = random.randint(1,10000)
            start6= int(time.time()*1000)
            radix(array)
            end6= int(time.time()*1000)
            total6 = end6 - start6
            file.write(str(total1)+","+str(total2)+","+str(total3)+","+str(total4)+","+str(total5)+","+str(total6)+"\n")

        file.close()

if __name__ == "__main__": main()
