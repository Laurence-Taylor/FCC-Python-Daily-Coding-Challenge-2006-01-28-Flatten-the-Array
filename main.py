def flatten(arr):
    # Create empty array
    arr_flat = []
    # for each element in the array
    for item in arr:
        # if element is an array then flatten and add to the flat array
        if isinstance(item, list):
            arr_flat += flatten(item)
        # else add element to the flat array
        else:
            arr_flat.append(item)

    return arr_flat

if __name__ == '__main__':
    print(flatten([1, [2, 3], 4]))
    print('=======')
    print(flatten([5, [4, [3, 2]], 1]))
    print('=======')
    print(flatten(["A", [[[["B"]]]], "C"]))
    print('=======')
    print(flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]]))
    print('=======')
    print(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]))