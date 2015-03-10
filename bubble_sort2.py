import random

def sort(items):
 # 1. TO DO: Implement a "bubble sort" routine here
    for outer in range(len(items)):
        for inner in range(len(items)-1-outer):
            if items[inner] > items[inner+1]:
                items[inner], items[inner+1] = items[inner+1], items[inner]     # Swap!
    return items 

numbers = list(range(10))
random.shuffle(numbers)

assert list(range(10)) == sort(numbers)
print("The list was sorted correctly!")

# 2. Change this print statement to display the complexity category.
# Refer to the cheat sheet in week9-class for examples.
print("This algorithm is classified as: O(n^2)")
