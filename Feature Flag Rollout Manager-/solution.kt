fun getFeatureAccess(
    userIds: List<Int>,
    rolloutPercentage: Int
): List<Boolean> {

    return userIds.map { userId ->
        (userId % 100) < rolloutPercentage
    }
}

fun main() {

    val userIds = listOf(
        101,
        205,
        310,
        450
    )

    val rolloutPercentage = 20

    val result =
        getFeatureAccess(
            userIds,
            rolloutPercentage
        )

    println(result)
}
