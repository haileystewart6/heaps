def running_medians_naive(iterable):
    values = []
    medians = []
    for i, x in enumerate(iterable):
        values.append(x)
        values.sort()
        if i%2 == 0:
            medians.append(values[i//2])
        else:
            medians.append((values[i//2] + values[i//2+1]) / 2)
    return medians
  
running_medians_naive([3, 1, 9, 25, 12])
running_medians_naive([8, 4, 11, 18])


def running_medians(iterable):
    medians = []
    min_heap = Heap(lambda x:-x)
    max_heap = Heap()
    temp_median = 0
    for i, x in enumerate(iterable):
        if 1 < (len(min_heap.data)-len(max_heap.data)):
            pop_value = min_heap.pop()
            max_heap.add(pop_value)
            
        if len(max_heap.data) == len(min_heap.data):
            (min_heap.peek()+max_heap.peek())/2 == temp_median
            
        elif (len(max_heap.data)-len(min_heap.data)) >1:
            pop_value = max_heap.pop()
            min_heap.add(pop_value)
            
        elif 1 == (len(min_heap.data)-len(max_heap.data)):
            temp_median = min_heap.peek()
            
        elif 1 == (len(max_heap.data) -len(min_heap.data)):
            temp_median = max_heap.peek()
            
        if x >= temp_median:
            min_heap.add(x)
        else:
            max_heap.add(x)
            
        medians.append(temp_median)
    return medians
