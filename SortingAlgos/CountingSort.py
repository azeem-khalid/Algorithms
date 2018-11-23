import random
import time
def countBucketSort(arr):

    countBucket = [0 for i in range(10)]

    output = [0 for i in range(len(arr))]

    for i in arr:
        countBucket[i] += 1

    ind =0

    for i in range(1,len(countBucket)):
        val = countBucket[i]
        for j in range(val):
            output[ind] = i
            ind+=1

    return output



file = open("CountingSort.csv","a")
for _ in range(10):
    input = [0 for i in range(10000)]
    for i in range(10000):
        input[i] = random.randint(1, 9)


    start = int(time.time()*1000)
    output = countBucketSort(input)
    end = int(time.time()*1000)
    total=end-start
    file.write(str(total) + ", ")

file.write("\n")