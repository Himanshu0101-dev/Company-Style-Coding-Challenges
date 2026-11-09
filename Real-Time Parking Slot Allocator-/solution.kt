import java.util.PriorityQueue
import java.util.HashMap

class ParkingAllocator(private val n: Int) {

    private val availableSlots = PriorityQueue<Int>()
    private val occupied = HashMap<Int, Int>()

    init {
        for (i in 0 until n) {
            availableSlots.offer(i)
        }
    }

    fun park(carId: Int): Int {

        if (availableSlots.isEmpty()) {
            return -1
        }

        val slot = availableSlots.poll()
        occupied[carId] = slot

        return slot
    }

    fun leave(carId: Int) {

        val slot = occupied.remove(carId)
            ?: return

        availableSlots.offer(slot)
    }

    fun getOccupiedCount(): Int {
        return occupied.size
    }
}
