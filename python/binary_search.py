# https://www.educative.io/courses/coderust-hacking-the-coding-interview/k5qJx
import random

class search:

    def __init__(self, arr):
        self.arr = arr

    def binary_search(self, key):
        print (f'arr: {self.arr} key: {key}')
        #val = self.binary_search_helper(key, 0, len(self.arr))
        val = self.binary_search_helper_iterative(key, 0, len(self.arr))
        return val

    def binary_search_helper(self, key, low, high):
        if low > high:
            return -1
        #why this variant https://leetcode.com/problems/guess-number-higher-or-lower/discuss/84662/What-is-the-difference-between-(low-%2B-high)-2-and-low-%2B-(high-low)-2
        #to avoid overflow
        mid = low + ((high-low)//2)

        if self.arr[mid] == key:
            return mid
        if key < self.arr[mid]:
            return self.binary_search_helper(key, low, mid-1)
        else:
            return self.binary_search_helper(key, mid+1, high)

    def binary_search_helper_iterative(self, key, low, high):

        while low <= high:
            mid = low + ((high-low)//2)

            if self.arr[mid] == key:
                return mid
            if key < self.arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


def populate_arr(arr: list, size: int):
    for i in range(size):
        arr.append(random.randint(0,size))
    return sorted(arr)

### main code
arr = []
arr = populate_arr(arr, 10)
s = search(arr)
print(s.binary_search(random.randint(0, 10)))
