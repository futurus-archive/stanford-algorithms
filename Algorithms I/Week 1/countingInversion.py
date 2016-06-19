inversions = 0


# merge sort code from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html

def mergeSort(alist):
    global inversions

    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
                inversions += len(lefthalf[i:])
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


f = open('IntegerArray.txt', 'r')
integers = []
for line in f:
    integers.append(int(line))

# alist = [5,1,3,4,2,6]
mergeSort(integers)
print(inversions)
