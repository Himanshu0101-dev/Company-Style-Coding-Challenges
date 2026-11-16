fun main() {

    val transcript = listOf(
        "Rahul: I'll complete authentication by Friday",
        "Priya: I will prepare API documentation by Monday",
        "Manager: Urgent deploy payment service by tomorrow"
    )

    val extractor = MeetingActionExtractor()

    val tasks = extractor.extract(transcript)

    tasks.forEach {
        println(it)
    }
}
