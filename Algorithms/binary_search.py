def binary_search(item, sequence):
    """
    sequence = [2, 6, 7, 8, 9, 12, 20, 42]
    item = 20
    """
    start_index = 0
    end_index = len(sequence)-1

    while start_index <= end_index:
        mid_index = start_index + (end_index-start_index) // 2
        if sequence[mid_index] == item:
            return mid_index
        elif item < sequence[mid_index]:
            end_index = mid_index - 1

        else:
            start_index = mid_index + 1

    return None


def binary_search_recursive(item, start, end, sequence):
    if start <= end:
        mid_index = (start + end) // 2
        if sequence[mid_index] == item:
            return mid_index
        elif sequence[mid_index] > item:
            return binary_search_recursive(item, start, mid_index-1, sequence)
        else:
            return binary_search_recursive(item, mid_index+1, end, sequence)

    else:
        return None
