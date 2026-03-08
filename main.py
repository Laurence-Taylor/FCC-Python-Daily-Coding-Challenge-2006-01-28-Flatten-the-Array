def flatten(arr):
    arr_flat = []
    for item in arr:
        if isinstance(item, list):
            flattern(item)
        else:
            arr_flat += item

    return arr_flat

if __name__ == '__main__':
    print(flatten([1, [2, 3], 4]))
    print('=======')
    print(flatten([5, [4, [3, 2]], 1]))
    print('=======')
    print(flatten(["A", [[[["B"]]]], "C"]))
    print('=======')gti 
    print(flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]]))
    print('=======')
    print(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]))