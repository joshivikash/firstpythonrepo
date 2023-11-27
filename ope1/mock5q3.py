import time
def insert(sorted_list,e):
    '''This will insert an element in the sorted list, without disturbing the existing list'''
    # When the list has only one element
    if len(sorted_list) == 0:
        return [e]
    # When the list has only one element
    if len(sorted_list) == 1:
        if e > sorted_list[0]:
            return sorted_list + [e]
        else:
            return [e] + sorted_list
    start_index = 0
    end_index = len(sorted_list) - 1
    mid_index = (end_index + start_index) // 2
    while True:
        if e == sorted_list[mid_index]:
            return sorted_list[:mid_index] + [e] + sorted_list[mid_index:]
        if e > sorted_list[mid_index]:
            start_index = mid_index + 1
        if e < sorted_list[mid_index]:
            end_index = mid_index - 1
        if end_index > start_index:
            mid_index = (end_index + start_index) // 2
        else:
            break
    if start_index == end_index:
        mid_index = start_index
    if e >= sorted_list[mid_index]:
        return sorted_list[:mid_index+1] + [e] + sorted_list[mid_index + 1: ]
    else:
        return sorted_list[:mid_index] + [e] + sorted_list[mid_index:]

    
limit = 100000000
sorted_list = []
print('populating the list...')
for i in range(limit):
    sorted_list.append(i)
print('inserting...')
a = time.time()
insert(sorted_list,limit)
b = time.time()
print('time taken for inserting the element {}'.format(b - a))