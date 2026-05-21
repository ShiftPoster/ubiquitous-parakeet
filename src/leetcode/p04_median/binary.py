# TODO: make sure to short circuit on both same median


def binary_search(arr: list[int], target: int) -> int:
    low = 0
    high = len(arr) - 1
    found = -1

    while low <= high:
        mid = (low + high) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            found = mid
            break
        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        # If target is smaller, ignore right half
        else:
            high = mid - 1

    # Target was not present in the array
    return found


[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 1, 1, 1, 2, 3, 3, 3, 3]


def find_above(array: list[int], target: int) -> int:
    low = 0
    high = len(array) - 1
    found = -1


    while low <= high:
        mid = (low + high) // 2
        right = mid - 1

        if array[mid] > target:
            # found new ceiling
            # if right >= 0:
            #     if array[right] <=
            high = mid + 1
        elif array[mid] < target:
            pass



        if array[mid] > target:
            right_i = mid - 1
            if right < 0:
                ...
            elif array[right_i] < target:
                found = mid



        # Check if target is present at mid
        if array[mid] == target:
            found = mid
            break
        # If target is greater, ignore left half
        elif array[mid] < target:
            low = mid + 1
        # If target is smaller, ignore right half
        else:
            high = mid - 1
            
    # Target was not present in the array
    return found
