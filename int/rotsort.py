


def search(arr, val):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) / 2

        if arr[mid] == val:
            return mid
        elif arr[start] <= arr[mid]:
            if val >= arr[start] and val < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if val > arr[mid] and val <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

import random

for _ in xrange(0, 100):
    n1 = random.randint(1, 100)
    n2 = random.randint(101, 200)
    arr = range(n1, n2) + range(0, n1)
    k = arr[random.randint(0, len(arr) - 1)]
    assert search(arr, k) == arr.index(k)

