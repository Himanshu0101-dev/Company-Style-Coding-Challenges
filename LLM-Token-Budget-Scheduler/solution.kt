import java.util.*

fun main() {
    val n = readLine()!!.toInt()
    val k = readLine()!!.toInt()

    val arr = readLine()!!
        .split(" ")
        .map { it.toInt() }
        .sorted()
        .toMutableList()

    var left = 0
    var right = n - 1
    var batches = 0

    while (left <= right) {

        if (left != right && arr[left] + arr[right] <= k) {
            left++
        }

        right--
        batches++
    }

    println(batches)
}
