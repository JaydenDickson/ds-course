def merge(items, sections, temporary_storage):
    (first_section_start, first_section_end), (
        second_section_start,
        second_section_end,
    ) = sections

    left_index = first_section_start
    right_index = second_section_start
    temp_index = 0

    # Merge both sections
    while left_index < first_section_end or right_index < second_section_end:
        if left_index < first_section_end and right_index < second_section_end:
            if len(items[left_index]) < len(items[right_index]):  #changed this line to compare the length of the strings instead of the strings themselves
                temporary_storage[temp_index] = items[left_index]
                left_index += 1
            else:
                temporary_storage[temp_index] = items[right_index]
                right_index += 1
            temp_index += 1

        elif left_index < first_section_end:
            for i in range(left_index, first_section_end):
                temporary_storage[temp_index] = items[left_index]
                left_index += 1
                temp_index += 1

        else:
            for i in range(right_index, second_section_end):
                temporary_storage[temp_index] = items[right_index]
                right_index += 1
                temp_index += 1

    # Copy back to original list
    for i in range(temp_index):
        items[first_section_start + i] = temporary_storage[i]

def merge_sort(items):
    # Get the length of the input list
    items_length = len(items)

    # Create temporary storage for merging
    temporary_storage = [None] * items_length

    # Initialise the size of subsections to 1
    size_of_subsections = 1

    # Iterate until the size of subsections is less than the length of the list
    while size_of_subsections < items_length:
        # Iterate over the list in steps of size_of_subsections * 2
        for i in range(0, items_length, size_of_subsections * 2):
            # Determine the start and end indices of the two subsections to merge
            first_section_start, first_section_end = i, min(
                i + size_of_subsections, items_length
            )
            second_section_start, second_section_end = first_section_end, min(
                first_section_end + size_of_subsections, items_length
            )

            # Define the sections to merge
            sections = (first_section_start, first_section_end), (
                second_section_start,
                second_section_end,
            )

            # Call the merge function
            merge(items, sections, temporary_storage)

        # Double subsection size each iteration
        size_of_subsections *= 2

    return items

fruits = ["apple", "banana", "kiwi", "grapefruit", "fig", "date", "elderberry", "honeydew", "jackfruit", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry"]
cars = ["ford", "audi", "mercedes", "bmw", "honda", "toyota", "nissan", "volkswagen", "hyundai", "kia", "subaru", "mazda", "volvo", "jaguar", "porsche", "ferrari", "lamborghini", "mclaren", "bugatti", "koenigsegg"]
games = ["chess", "checkers", "go", "backgammon", "scrabble", "monopoly", "risk", "clue", "catan", "carcassonne"]

sorted_fruits = merge_sort(fruits)
sorted_cars = merge_sort(cars)
sorted_games = merge_sort(games)
print(sorted_fruits)
print(sorted_cars)
print(sorted_games)