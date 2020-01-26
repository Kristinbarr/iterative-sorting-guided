# searching with Artem Litchmanov

names = [
    "Artem",
    "Austin",
    "Chad",
    "Dustin",
    "Elissa",
    "Emily",
    "Jamar",
    "Katherine",
    "Kyran",
    "Justin",
    "Levi",
    "Reed",
    "Ronny",
    "Wilfred",
    "Yasirah"
]


def linear_search(array, value):
    for name in array:
        if name == value:
            return True
    return False

#


def binary_search(array, value):
    # keep track of start, end and if found
    start = 0
    end = len(array) - 1
    found = False
    while not found and start <= end:
        # start in the middle
        middle = (start + end) // 2
        print("MIDDLE: ", middle)
        # compare value to search val
        if array[middle] == value:
            print(f"position: {middle}")
            found = True
        else:
        # if lower, remove right side
            if value < array[middle]:
                end = middle - 1
                print('val is smaller:', start, end, found)
            # if higher, remove left side
            else:
                start = middle + 1
                print('val is bigger:', start, end, found)
    return value, found


# print(linear_search(names, "Katherine"))
# print()
# print(linear_search(names, "Ronny"))
# print()
# print(linear_search(names, "Justin"))
# print()

print(binary_search(names, "Katherine"))
print()
print(binary_search(names, "Ronny"))
print()
print(binary_search(names, "Justin"))
print()
