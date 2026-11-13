import kotlin.test.Test
import kotlin.test.assertEquals

class AICacheTest {

    @Test
    fun `evicts lowest cost first`() {
        val cache = AICache(3)
        cache.put("a", 10, 1)
        cache.put("b", 4, 2)
        cache.put("c", 8, 3)

        assertEquals("b", cache.evict())
    }

    @Test
    fun `breaks cost tie using oldest timestamp`() {
        val cache = AICache(3)
        cache.put("x", 5, 10)
        cache.put("y", 5, 4)
        cache.put("z", 5, 7)

        assertEquals("y", cache.evict())
    }

    @Test
    fun `breaks full tie using smallest key`() {
        val cache = AICache(3)
        cache.put("banana", 5, 10)
        cache.put("apple", 5, 10)
        cache.put("cherry", 5, 10)

        assertEquals("apple", cache.evict())
    }

    @Test
    fun `get refreshes timestamp`() {
        val cache = AICache(2)
        cache.put("old", 5, 1)
        cache.put("new", 5, 2)

        assertEquals(5, cache.get("old"))

        cache.put("replacement", 5, 3)
        assertEquals("new", cache.evict())
    }

    @Test
    fun `put updates existing entry`() {
        val cache = AICache(2)
        cache.put("a", 10, 1)
        cache.put("b", 6, 2)

        cache.put("a", 3, 5)

        assertEquals("b", cache.evict())
    }

    @Test
    fun `empty cache returns blank key`() {
        val cache = AICache(2)
        assertEquals("", cache.evict())
    }

    @Test
    fun `zero capacity ignores puts`() {
        val cache = AICache(0)
        cache.put("a", 10, 1)

        assertEquals(-1, cache.get("a"))
        assertEquals("", cache.evict())
    }
}
