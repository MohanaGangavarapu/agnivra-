# Combined Program: Sort list using Bubble Sort and search using Binary Search

'''
Description:
This program sorts an unsorted list using Bubble Sort,
then performs Binary Search to find a user-specified target value.

Example:
Input: 9 2 5 1 7
Target: 5
Output:
Sorted list: [1, 2, 5, 7, 9]
Binary Search: Found at index 2
'''

# Input
arr = list(map(int, input("Enter unsorted numbers: ").split()))
target = int(input("Enter target number: "))

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

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

# Run functions
sorted_arr = bubble_sort(arr)
print("Sorted list:", sorted_arr)

index = binary_search(sorted_arr, target)
print("Binary Search:", f"Found at index {index}" if index != -1 else "Not found")
