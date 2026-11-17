import kotlin.math.sqrt

data class Driver(
    val id: String,
    var x: Int,
    var y: Int,
    var available: Boolean = true
)

data class Order(
    val id: String,
    val x: Int,
    val y: Int
)

class DeliveryAssignmentSystem {

    private fun distance(
        x1: Int,
        y1: Int,
        x2: Int,
        y2: Int
    ): Double {
        return sqrt(
            ((x1 - x2) * (x1 - x2) +
             (y1 - y2) * (y1 - y2)).toDouble()
        )
    }

    fun assignOrder(
        order: Order,
        drivers: MutableList<Driver>
    ) {

        var nearestDriver: Driver? = null
        var minDistance = Double.MAX_VALUE

        for (driver in drivers) {

            if (!driver.available) continue

            val currentDistance = distance(
                order.x,
                order.y,
                driver.x,
                driver.y
            )

            if (currentDistance < minDistance) {
                minDistance = currentDistance
                nearestDriver = driver
            }
        }

        if (nearestDriver != null) {
            nearestDriver.available = false

            println(
                "Order ${order.id} assigned to Driver ${nearestDriver.id}"
            )
        } else {
            println("No available driver for Order ${order.id}")
        }
    }

    fun completeDelivery(driver: Driver) {
        driver.available = true
        println("Driver ${driver.id} is now available")
    }
}

fun main() {

    val drivers = mutableListOf(
        Driver("D1", 10, 20),
        Driver("D2", 15, 25),
        Driver("D3", 30, 40)
    )

    val orders = listOf(
        Order("O1", 13, 22),
        Order("O2", 32, 45)
    )

    val system = DeliveryAssignmentSystem()

    for (order in orders) {
        system.assignOrder(order, drivers)
    }
}
