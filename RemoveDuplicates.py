# Program to remove duplicates from a user-input list of numbers

'''
Description:
This program takes a list of numbers from the user (separated by spaces),
removes any duplicate numbers, and outputs a list containing only unique numbers
in the order they first appeared.

Example:
Input: 4 5 6 4 7 5 8
Output: [4, 5, 6, 7, 8]
'''

# Step 1: Get input from user as a string and split into list of strings
user_input = input("Enter numbers separated by spaces: ").split()

# Step 2: Convert each input string to an integer
numbers = [int(num) for num in user_input]

# Step 3: Create an empty list to store unique numbers
unique_numbers = []

# Step 4: Iterate through the numbers list
for num in numbers:
    # If the number is not already in unique_numbers, append it
    if num not in unique_numbers:
        unique_numbers.append(num)

# Step 5: Print the list of unique numbers
print("List after removing duplicates:", unique_numbers)
