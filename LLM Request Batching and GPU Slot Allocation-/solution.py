import heapq

def min_gpus_required(requests):
    requests.sort(key=lambda x: x[0])

    gpu_heap = []

    for start, end in requests:

        if gpu_heap and gpu_heap[0] <= start:
            heapq.heappop(gpu_heap)

        heapq.heappush(gpu_heap, end)

    return len(gpu_heap)


# Example
requests = [
    [1, 4],
    [2, 5],
    [7, 9],
    [3, 6]
]

print(min_gpus_required(requests))
