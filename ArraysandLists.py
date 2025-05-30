# Program to find the largest number in a list using user input

'''Description:
This program asks the user to enter a list of numbers separated by spaces. It then finds and prints the largest number in that list by comparing each element.

Example input:
12 45 7 89 34

Example output:
The largest number is: 89'''


# Step 1: Take input from the user and convert it into a list of integers
# User inputs numbers separated by space
numbers = input("Enter numbers separated by spaces: ").split()

# Step 2: Convert each number from string to integer
numbers = [int(num) for num in numbers]

# Step 3: Initialize the first number as the largest
largest = numbers[0]

# Step 4: Traverse the list to find the largest number
for num in numbers:
    if num > largest:
        largest = num  # update if current number is greater

# Step 5: Display the result
print("The largest number is:", largest)

