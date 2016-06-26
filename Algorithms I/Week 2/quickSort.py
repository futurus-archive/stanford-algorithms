f = open('QuickSort.txt', 'r')
integers = []
for line in f:
    integers.append(int(line))


def quicksort(array, start, end):
    # Base case: an array of size 1 or 0 is considered sorted => no comparison
    if ((end - start) < 2):
        return 0;

    # number of comparisons = m - 1 where m is the size of subarray
    comparisons = end - start - 1;

    # get median's index and do a quick preprocessing step
    med = median(array, start, end)
    array[start], array[med] = array[med], array[start]

    # uncomment next line for final element as pivot
    # array[end-1], array[start] = array[start], array[end-1]

    # Set the pivot to always be the first element of the array.
    pivot = start;

    # Set boundaries for the left and the right markers: i marks less than pivot, j marks greater than pivot
    i = start + 1;

    # Partition around the pivot.
    for j in range(start + 1, end):
        if (array[j] < array[pivot]):
            array[i], array[j] = array[j], array[i]
            i += 1

    # Put the pivot in its correct place.
    array[i - 1], array[pivot] = array[pivot], array[i - 1]

    # Recursively calculate the number of comparisons in left and right subarrays
    comparisons += quicksort(array, start, i - 1)
    comparisons += quicksort(array, i, end)

    return comparisons;


def median(array, start, end):
    first = array[start];
    middle = array[start + (end - 1 - start) / 2];
    last = array[end - 1];

    mx = max(first, middle, last);
    mn = min(first, middle, last);

    # using bitwise operator trick to get the median element
    # a ^ a = 0 for all a
    return array.index(first ^ middle ^ last ^ mx ^ mn)


# pivot = first # => 162085
# pivot = final # => 164123
# pivot = median # => 138382

print quicksort(integers, 0, len(integers))
