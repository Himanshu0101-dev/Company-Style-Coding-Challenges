class Node(
    var key: String,
    var value: String
) {
    var prev: Node? = null
    var next: Node? = null
}

class LRUCache(private val capacity: Int) {

    private val cache = HashMap<String, Node>()

    private val head = Node("", "")
    private val tail = Node("", "")

    init {
        head.next = tail
        tail.prev = head
    }

    private fun addNode(node: Node) {
        node.next = head.next
        node.prev = head

        head.next?.prev = node
        head.next = node
    }

    private fun removeNode(node: Node) {
        node.prev?.next = node.next
        node.next?.prev = node.prev
    }

    private fun moveToFront(node: Node) {
        removeNode(node)
        addNode(node)
    }

    fun get(prompt: String): String? {

        val node = cache[prompt] ?: return null

        moveToFront(node)

        return node.value
    }

    fun put(prompt: String, response: String) {

        if (cache.containsKey(prompt)) {

            val node = cache[prompt]!!
            node.value = response

            moveToFront(node)

        } else {

            val newNode = Node(prompt, response)

            cache[prompt] = newNode
            addNode(newNode)

            if (cache.size > capacity) {

                val lru = tail.prev!!

                removeNode(lru)
                cache.remove(lru.key)
            }
        }
    }

    fun displayCache() {

        var current = head.next

        while (current != tail) {
            print("${current!!.key} -> ")
            current = current.next
        }

        println("END")
    }
}

fun main() {

    val cache = LRUCache(3)

    cache.put("What is AI?", "Artificial Intelligence")
    cache.put("What is ML?", "Machine Learning")
    cache.put("What is NLP?", "Natural Language Processing")

    println(cache.get("What is AI?"))

    cache.put("What is GenAI?", "Generative AI")

    cache.displayCache()
}
