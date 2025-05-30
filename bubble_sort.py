# Program to implement Bubble Sort

'''
Description:
This program sorts a list of numbers using the Bubble Sort algorithm.
It repeatedly steps through the list, compares adjacent items, and swaps them
if they are in the wrong order.

Example:
Input: 5 3 8 4 2
Output: Sorted list: [2, 3, 4, 5, 8]
'''

# Step 1: Take input from user
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Step 2: Bubble Sort implementation
n = len(nums)
for i in range(n):
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]  # Swap

# Step 3: Output sorted list
print("Sorted list:", nums)
