def bubbleSearch(list):
    end_index = len(list)-1
    done = False
    while not done:
        done = True
        for i in range(0, end_index):
            if list[i] > list[i+1]:
                done = False
                list[i], list[i+1] = list[i+1], list[i]
    return list


print(bubbleSearch([1, 5, 9, 3, 4, 7, 21, 81, 31, 35, 84, 32]))
