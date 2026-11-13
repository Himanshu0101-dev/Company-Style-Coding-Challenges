# Problem statement
An AI company runs a caching service for expensive model responses. Each cached response has:
a unique key
a timestamp when it was last used
a cost representing the compute cost to regenerate it
When the cache reaches its capacity, it must evict entries using a custom policy:
Evict the entry with the lowest cost first.
If multiple entries have the same lowest cost, evict the one with the oldest last-used timestamp.
If cost and timestamp are both equal, evict the lexicographically smallest key.
Implement the AICache class:
# class AICache(private val capacity: Int) {
    fun put(key: String, cost: Int, timestamp: Int)
    fun get(key: String): Int  // returns cost, or -1 if absent
    fun evict(): String        // returns evicted key, or "" if empty
}
put inserts or updates an entry. Updating an entry must refresh its timestamp and cost.
get returns the entry’s cost and refreshes its timestamp to the current value supplied by the caller.
evict removes and returns the key selected by the eviction policy.
If capacity is 0, put should do nothing and evict should return "".
# exmaple 
kotlin
val cache = AICache(2)
cache.put("prompt-a", cost = 10, timestamp = 1)
cache.put("prompt-b", cost = 5, timestamp = 2)
cache.get("prompt-a") // returns 10
cache.put("prompt-c", cost = 7, timestamp = 3)
cache.evict()         // returns "prompt-b"

# Explanation:
"prompt-a" has cost 10.
"prompt-b" has cost 5.
"prompt-c" has cost 7.
The lowest-cost entry is "prompt-b", so it is evicted.

# constraints
1 <= capacity <= 10^5
1 <= cost <= 10^9
0 <= timestamp <= 10^9
key contains only lowercase English letters and digits.
At most 10^5 total operations.
Timestamps may not be increasing, so the cache must store the latest timestamp explicitly rather than relying on insertion order.
