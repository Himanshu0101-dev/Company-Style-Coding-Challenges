class MeetingActionExtractor {

    private val dueDateRegex =
        Regex("\\b(today|tomorrow|monday|tuesday|wednesday|thursday|friday|saturday|sunday)\\b",
            RegexOption.IGNORE_CASE)

    fun extract(transcript: List<String>): List<ActionItem> {

        val result = mutableListOf<ActionItem>()

        for (line in transcript) {

            val parts = line.split(":", limit = 2)

            if (parts.size < 2) continue

            val speaker = parts[0].trim()
            val statement = parts[1].trim()

            if (containsTask(statement)) {

                val dueDate =
                    dueDateRegex.find(statement)?.value ?: "Not Specified"

                val priority =
                    if (statement.contains("urgent", true) ||
                        statement.contains("asap", true))
                        "High"
                    else
                        "Medium"

                result.add(
                    ActionItem(
                        assignee = speaker,
                        task = extractTask(statement),
                        dueDate = dueDate,
                        priority = priority
                    )
                )
            }
        }

        return result
    }

    private fun containsTask(text: String): Boolean {

        val keywords = listOf(
            "i will",
            "i'll",
            "complete",
            "prepare",
            "create",
            "finish",
            "submit",
            "deploy",
            "implement"
        )

        return keywords.any {
            text.contains(it, true)
        }
    }

    private fun extractTask(text: String): String {

        return text
            .replace("I'll", "", true)
            .replace("I will", "", true)
            .replace("by", "", true)
            .trim()
    }
}
