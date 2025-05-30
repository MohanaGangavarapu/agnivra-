# Program to implement Linear Search and Binary Search

'''
Description:
This program demonstrates both Linear Search and Binary Search.
Linear Search checks each element one by one.
Binary Search requires a sorted list and uses divide-and-conquer.

Example Input: 2 4 6 8 10
Target: 6
Output: 
Linear Search: Found at index 2
Binary Search: Found at index 2
'''

# Step 1: Take input
arr = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter number to search: "))

# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Outputs
print("Linear Search:", "Found at index" if (i := linear_search(arr, target)) != -1 else "Not found", i)
print("Binary Search:", "Found at index" if (j := binary_search(arr, target)) != -1 else "Not found", j)
