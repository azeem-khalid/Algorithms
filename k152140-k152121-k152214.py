## Algorithm Project
## Team Members:
## Sameer 15k-2140
## Munesh Kumar 15k-2121
## Muhammad Yasir 15k-2214


import sys
from collections import defaultdict
import os
import random
import time
def insertionSort(array):
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


def bubbleSort(mylist):
    for i in range(len(mylist)-1,0,-1):
        for j in range(i):
            if mylist[j] > mylist[j+1]:
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp


def selectionSort(mylist):
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
 

def radixSort(arr):
 

    max1 = max(arr)
 

    exp = 1
    while max1//exp > 0:
        countingSort(arr,exp)
        exp *= 10



def matrixChainOrder(arrayOfMatrix):
    n = len(arrayOfMatrix)
    m = [[0 for i in range(n)] for i in range(n)]

    for i in range(0,n):
        m[i][i] = 0

    for l in range(2,n):
        for i in range(n-l+1):
            j = i+l-1
            m[i][j] = sys.maxsize
            for k in range(i,j):
                q = m[i][k]+m[k+1][j]+arrayOfMatrix[i-1]*arrayOfMatrix[k]*arrayOfMatrix[j]
                if q < m[i][j]:
                    m[i][j] = q
    return m[1][n-1]


def knapSack(W, wt, val, n):
    K = [[0 for i in range(W+1)] for j in range(n+1)]
 
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                K[i][j] = 0
            elif wt[i-1] <= j:
                K[i][j] = max(val[i-1] + K[i-1][j-wt[i-1]],  K[i-1][j])
            else:
                K[i][j] = K[i-1][j]
 
    return K[n][W]


## DFS traversal

def newEdge(graph,u,v):
    graph[u].append(v)

def DFSHelper(graph,v,visited):
    visited[v]= True
    print(v)
    for i in graph[v]:
        if visited[i] == False:
            DFSHelper(graph,i, visited)


def DFS(graph,v):
    visited = [False]*(len(graph))
    DFSHelper(graph,v,visited)


## DFS Ends

## BFS Traversal

def newEdge(graph,u,v):
    graph[u].append(v)

def BFS(graph, s):
    visited = [False]*(len(graph))
    queue = []
    queue.append(s)
    visited[s] = True
    while queue:
        s = queue.pop(0)
        print(s),
        for i in graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
## BFS Ends

## Prims Algorithm

def display1(graph , noOfVertices , parent):
    print("Edge \tWeight")
    for i in range(1,noOfVertices):
        print(parent[i],"-",i,"\t",graph[i][parent[i]])

def minValue(noOfVertices , key , mstSet):
    min = sys.maxsize;
    for v in range(noOfVertices):
        if key[v] < min and mstSet[v] == False:
            min = key[v]
            min_index = v
    return min_index

def Prims(graph , noOfVertices):

    key = [sys.maxsize] * noOfVertices
    parent = [None] * noOfVertices
    key[0] = 0
    mstSet = [False] * noOfVertices
    parent[0] = -1

    for c in range(noOfVertices):
        u = minValue(noOfVertices , key , mstSet)
        mstSet[u] = True
        for v in range(noOfVertices):
            if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u
    display1(graph , noOfVertices , parent)


## Prims End

## Kruskal Algorithm

def addEdge(graph,u,v,w):
    graph.append([u,v,w])

def find(parent,i):
    if parent[i] == i:
        return i
    return find(parent,parent[i])

def doUnion(parent,rank,a,b):
    aroot = find(parent,a)
    broot = find(parent,b)
    if rank[aroot] < rank[broot]:
        parent[aroot] = broot
    elif rank[aroot] > rank[broot]:
        parent[broot] = aroot
    else:
        parent[broot] = aroot
        rank[aroot] += 1
def Kruskal(graph , vertices):
    resultant = []

    i=0
    r=0

    graph = sorted(graph,key=lambda item:item[2])
    parent = []
    rank = []

    for j in range(vertices):
        parent.append(j)
        rank.append(0)

    while r < vertices-1:
        u,v,w = graph[i]
        i=i+1
        a = find(parent,u)
        b = find(parent,v)
        if a != b:
            r = r+1
            resultant.append([u,v,w])
            doUnion(parent,rank,a,b)
    print("Resultant MST is [u,v,w]")
    print(resultant)



## kruskal Ends


## Bellman Ford Algorithm


def newEdge(graph,u,v,w):
    graph.append([u, v, w])

def display(noOfVertices, distance):
    print("Vertex   Distance from Source")
    for i in range(noOfVertices):
        print("{} \t\t {}".format(i, distance[i]))

def BellmanFord(graph , noOfVertices , source):
    
    distance = [float("Inf")] * noOfVertices
    distance[source] = 0
    for i in range(noOfVertices - 1):
        for u, v, w in graph:
            if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

    for u, v, w in graph:
            if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                    print("Graph contains negative weight cycle")
                    return
    display(noOfVertices , distance)


## Bellman Ends

## Dijkstra Algorithm


def display(noOfVertices, distance):
    print("Vertex\tDistance from Source")
    for i in range(noOfVertices):
        print(i,"\t",distance[i])
        
def minDistance(noOfVertices, distance, sptSet):
    min = sys.maxsize
    for i in range(noOfVertices):
        if distance[i] < min and sptSet[i] == False:
            min = distance[i]
            min_index = i
    return min_index

def dijkstra(graph , noOfVertices, source):
    distance = [sys.maxsize] * noOfVertices
    distance[source] = 0
    sptSet = [False] * noOfVertices
    
    for i in range(noOfVertices):
        u = minDistance(noOfVertices , distance, sptSet)
        sptSet[u] = True
        for v in range(noOfVertices):
            if graph[u][v] > 0 and sptSet[v] == False and distance[v] > distance[u] + graph[u][v]:
                    distance[v] = distance[u] + graph[u][v]
    display(noOfVertices , distance)

## Dijkstra Ends






def main():
    print('Algorithm Implementation')
    print('Menu')
    print('1- Sorting Algorithm')
    print('2- Matrix chain Order')
    print('3- 0-1 Knapsack Problem')
    print('4- Graph Traversal')
    print('5- MST Algorithm')
    print('6- Shorthest path Algorithm')
    print('7- Create CSV File')
    
    choice1 = int(input('Enter your choice: '))
    if choice1 == 1:
        totalInput = int(input('Enter total number of inputs: '))
        array = [0 for i in range(totalInput)]
        print('Enter the inputs: ')
        for i in range(totalInput):
            array[i] = int(input())
        print()
        print('1-Bubble Sort')
        print('2-Insertion Sort')
        print('3-Selection Sort')
        print('4-Merge Sort')
        print('5-Counting Sort')
        print('6-Radix Sort')
        choice2 = int(input('Select from sorting algorithms: '))
        if choice2 == 1:
            bubbleSort(array)
        elif choice2 == 2:
            insertionSort(array)
        elif choice2 == 3:
            selectionSort(array)
        elif choice2 == 4:
            mergeSort(array,0,len(array)-1)
        elif choice2 == 5:
            array = countSort(array)
        elif choice2 == 6:
            radixSort(array)
        else:
            print('Incorrect choice')
            sys.exit()
        print('Resulting array is: ')
        for i in array:
            print(i,end=' ')
    elif choice1 == 2:
        j=0
        totalMatrix = int(input('Enter total number of matrices: '))
        matrixDim = [0 for i in range(2*totalMatrix)]
        print('Enter the dimensions for the matrices')
        for i in range(totalMatrix):
            matrixDim[j] = int(input('Enter Total rows for matrix {} : '.format(i+1)))
            j+=1
            matrixDim[j] = int(input('Enter Total columns for matrix {} : '.format(i+1)))
            j+=1

        for i in range(1,len(matrixDim)-1,2):
            if matrixDim[i] != matrixDim[i+1]:
                print('Matrix cannot be multiplied')
                sys.exit()

        matrixDim1 = [0 for i in range(totalMatrix+1)]
        matrixDim1[0] = matrixDim[0]
        j=1
        for i in range(1,len(matrixDim),2):
            matrixDim1[j] = matrixDim[i]
            j+=1

        result = matrixChainOrder(matrixDim1)
        print('Minimum cost to multiply these matrices is {}'.format(result))
    elif choice1 == 3:
        totalVal = int(input('Enter total number of value array: '))
        totalWt = totalVal
        val = [0 for i in range(totalVal)]
        wt = [0 for j in range(totalWt)]
        print('Enter weight-value pairs: ')
        for i in range(totalVal):
            val[i] = int(input('Enter the value {}: '.format(i+1)))
            wt[i] = int(input('Enter the Weight {}: '.format(i+1)))
        W = int(input('Enter the maximum weight: '))
        result = knapSack(W,wt,val,totalVal)
        print('The maximum value that can be picked is {}'.format(result))
    elif choice1 == 4:
        graph = defaultdict(list)
        print()
        totalVertices = int(input('Enter total Vertices: '))
        totalEdges = int(input('Enter total Edges: '))
        for i in range(totalEdges):
            startingEdge = int(input('Enter starting vertex for the egde {}: '.format(i+1)))
            EndingEdge = int(input('Enter Ending vertex for the egde {}: '.format(i+1)))
            newEdge(graph, startingEdge, EndingEdge)

        s = int(input('Enter the starting vertex for traversal: '))
        
        print('1- DFS')
        print('2- BFS')
        choice2 = int(input('Enter Your choice: '))
        if choice2 == 1:
            print('Following is the DFS traversal of this graph: ')
            DFS(graph,s)
        elif choice2 == 2:
            print('Following is the BFS traversal of this graph: ')
            BFS(graph,s)
        else:
            print('Incorrect choice')
            sys.exit()
    elif choice1 == 5:
        print('1- Kruskal Algorithm')
        print('2- Prims Algorithm')
        choice3 = int(input('Enter your choice: '))
        if choice3 == 1:
            v = int(input("Enter the number of vertices : "))
            vertices = v
            graph = []
            ch = 'y'
            while ch != 'n':
                print("Enter input in the form u v w")
                u1 = int(input("Enter U: "))
                v1 = int(input("Enter V: "))
                w1 = int(input("Enter W: "))
                addEdge(graph , u1,v1,w1)
                ch = str(input("Do you want to continue (y/n): "))

            Kruskal(graph , v)

        elif choice3 == 2:
            noOfVertices = int(input('Enter total number of vertices: '))
            graph = [[0 for c in range(noOfVertices)] for r in range(noOfVertices)]
            print('Enter the Adjacency Matrix: ')
            for i in range(noOfVertices):
                for j in range(noOfVertices):
                    graph[i][j] = int(input('Enter weight for edge from {} to {}: '.format(i,j)))

            Prims(graph , noOfVertices)
        else:
            print('Incorrect Choice')
            sys.exit()
    elif choice1 == 6:
        print('1- Bellman Ford Algorithm')
        print('2- Dijkstra Algorithm')
        choice4 = int(input('Enter your choice: '))
        if choice4 == 1:
            noOfVertices = int(input('Enter total number of vertices: '))
            graph = []
            ch = 'y'
            while ch != 'n':
                print("Enter input in the form u v w")
                u2 = int(input("Enter U: "))
                v2 = int(input("Enter V: "))
                w2 = int(input("Enter W: "))
                addEdge(graph , u2,v2,w2)
                ch = str(input("Do you want to continue (y/n): "))
            s = int(input('Enter starting Vertex: '))

            BellmanFord(graph , noOfVertices , s)
        elif choice4 == 2:
            noOfVertices = int(input('Enter total number of vertices: '))
            graph = [[0 for c in range(noOfVertices)] for r in range(noOfVertices)]
            print('Enter the Adjacency Matrix: ')
            for i in range(noOfVertices):
                for j in range(noOfVertices):
                    graph[i][j] = int(input('Enter weight for edge from {} to {}: '.format(i+1,j+1)))

            s = int(input('Enter the starting vertex: '))

            dijkstra(graph , noOfVertices , s)

    elif choice1 == 7:
        file = open("CSVFile.txt","a")
        for i in range(10):
            array = [0 for i in range(10000)]
            for i in range(10000):
                array[i] = random.randint(1,10000)
            #time for bubble sort
            startBubble = int(time.time()*1000)
            bubbleSort(array)
            endBubble = int(time.time()*1000)
            totalBubble = endBubble - startBubble
            #time for Selection sort
            for i in range(10000):
                array[i] = random.randint(1,10000)
            startSelection = int(time.time()*1000)
            selectionSort(array)
            endSelection = int(time.time()*1000)
            totalSelection = endSelection - startSelection
            #time for insertion sort
            for i in range(10000):
                array[i] = random.randint(1,10000)
            startInsertion = int(time.time()*1000)
            insertionSort(array)
            endInsertion = int(time.time()*1000)
            totalInsertion = endInsertion - startInsertion
            #time for Merge sort
            for i in range(10000):
                array[i] = random.randint(1,10000)
            startMerge = int(time.time()*1000)
            mergeSort(array,0,len(array)-1)
            endMerge = int(time.time()*1000)
            totalMerge = endMerge - startMerge
            #time for Counting sort
            for i in range(10000):
                array[i] = random.randint(1,10000)
            startCounting = int(time.time()*1000)
            array = countSort(array)
            endCounting = int(time.time()*1000)
            totalCounting = endCounting - startCounting
            #time for Radix sort
            for i in range(10000):
                array[i] = random.randint(1,10000)
            startRadix = int(time.time()*1000)
            radixSort(array)
            endRadix = int(time.time()*1000)
            totalRadix = endRadix - startRadix
            file.write(str(totalBubble)+","+str(totalSelection)+","+str(totalInsertion)+","+str(totalMerge)+","+str(totalCounting)+","+str(totalRadix)+"\n")

        file.close()
    else:
        print('Incorrect choice')
        sys.exit()

if __name__ == "__main__": main()
