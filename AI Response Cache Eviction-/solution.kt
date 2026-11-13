import java.util.TreeSet

class AICache(private val capacity: Int) {

    private data class Entry(
        val key: String,
        val cost: Int,
        val timestamp: Int
    ) : Comparable<Entry> {

        override fun compareTo(other: Entry): Int {
            return compareValuesBy(
                this,
                other,
                { it.cost },
                { it.timestamp },
                { it.key }
            )
        }
    }

    private val entries = HashMap<String, Entry>()
    private val evictionOrder = TreeSet<Entry>()

    fun put(key: String, cost: Int, timestamp: Int) {
        if (capacity == 0) return

        entries[key]?.let { existing ->
            evictionOrder.remove(existing)
        }

        val updated = Entry(key, cost, timestamp)
        entries[key] = updated
        evictionOrder.add(updated)

        if (entries.size > capacity) {
            evict()
        }
    }

    fun get(key: String): Int {
        if (capacity == 0) return -1

        val entry = entries[key] ?: return -1

        // A real implementation would receive the current timestamp.
        // For this interface, retain the stored timestamp.
        return entry.cost
    }

    fun evict(): String {
        if (capacity == 0 || entries.isEmpty()) return ""

        val worst = evictionOrder.first()

        evictionOrder.remove(worst)
        entries.remove(worst.key)

        return worst.key
    }
}
