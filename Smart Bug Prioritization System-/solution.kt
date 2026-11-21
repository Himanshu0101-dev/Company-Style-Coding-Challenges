data class Bug(
    val id: Int,
    val severity: String,
    val impactedUsers: Int,
    val occurrences: Int
)

fun getSeverityValue(severity: String): Int {
    return when (severity) {
        "CRITICAL" -> 5
        "HIGH" -> 4
        "MEDIUM" -> 3
        "LOW" -> 2
        else -> 1
    }
}

fun main() {

    val n = readLine()!!.toInt()
    val bugs = mutableListOf<Pair<Bug, Int>>()

    repeat(n) {
        val input = readLine()!!.split(" ")

        val id = input[0].toInt()
        val severity = input[1]
        val impactedUsers = input[2].toInt()
        val occurrences = input[3].toInt()

        val severityValue = getSeverityValue(severity)

        val score =
            severityValue * 100 +
            impactedUsers * 5 +
            occurrences * 2

        bugs.add(
            Pair(
                Bug(id, severity, impactedUsers, occurrences),
                score
            )
        )
    }

    bugs.sortWith(
        compareByDescending<Pair<Bug, Int>> { it.second }
            .thenByDescending { it.first.impactedUsers }
            .thenBy { it.first.id }
    )

    bugs.forEach {
        println(it.first.id)
    }
}
