An AI company serves millions of requests. Each request asks for a model identified by an integer ID.
The server cache can hold at most K models.
If a requested model is already in cache, it is a cache hit.
Otherwise, it is a cache miss, and if the cache is full, one existing model must be removed.
Your task is to determine the minimum number of cache misses using the optimal replacement strategy.

# input 
requests = [1,2,3,2,1,4,1,2]
K = 3
# output
5
# example 
cache size = 3
Request 1 -> Miss
Request 2 -> Miss
Request 3 -> Miss
Request 2 -> Hit
Request 1 -> Hit
Request 4 -> Miss (evict 3)
Request 1 -> Hit
Request 2 -> Hit

Total Misses = 4
