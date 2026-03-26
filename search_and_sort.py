given_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
# Since the list is not sorted, we will linear search  
for i in range(len(given_list)):
    if given_list[i] == 9:
        print("Found 9 at index", i)
        break
else:
    print("9 not found in the list")
# Sort the list using insertion sort
def insertion_sort(items):
    sorted_list = []
    for item in items:
        sort_insert(item, sorted_list)

# Helper function to insert an item into the sorted list
def sort_insert(item, sorted_list):
    for i in range(len(sorted_list)):
        if item < sorted_list[i]:
            sorted_list.insert(i, item)
            break
    else:
        sorted_list.append(item)
    return sorted_list

insertion_sort(given_list)
print(given_list)

# Search given_list for 9 using binary search
def binary_search(items, target):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return "Not found"

print(binary_search(given_list, 9))
