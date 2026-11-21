fun main() {

    val warehouseCount = readLine()!!.toInt()

    val warehouse = mutableMapOf<String, Int>()

    repeat(warehouseCount) {
        val input = readLine()!!.split(" ")
        warehouse[input[0]] = input[1].toInt()
    }

    val websiteCount = readLine()!!.toInt()

    val website = mutableMapOf<String, Int>()

    repeat(websiteCount) {
        val input = readLine()!!.split(" ")
        website[input[0]] = input[1].toInt()
    }

    for ((product, warehouseStock) in warehouse) {

        val websiteStock = website[product] ?: 0

        if (warehouseStock != websiteStock) {

            val diff = warehouseStock - websiteStock

            println(
                "$product $warehouseStock $websiteStock $diff"
            )
        }
    }
}
