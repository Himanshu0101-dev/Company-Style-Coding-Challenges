def min_cache_misses(requests, k):
    cache = set()
    misses = 0

    for i in range(len(requests)):
        current = requests[i]

        # Cache Hit
        if current in cache:
            continue

        # Cache Miss
        misses += 1

        # Free Space Available
        if len(cache) < k:
            cache.add(current)
            continue

        # Find item to evict
        victim = None
        farthest_use = -1

        for model in cache:
            next_use = float('inf')

            for j in range(i + 1, len(requests)):
                if requests[j] == model:
                    next_use = j
                    break

            if next_use > farthest_use:
                farthest_use = next_use
                victim = model

        cache.remove(victim)
        cache.add(current)

    return misses


# Example Usage
requests = [1, 2, 3, 2, 1, 4, 1, 2]
k = 3

print("Minimum Cache Misses:", min_cache_misses(requests, k))
