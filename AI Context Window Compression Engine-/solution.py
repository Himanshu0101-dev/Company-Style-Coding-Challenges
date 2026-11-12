from collections import deque


class ContextCompressor:

    def __init__(self, token_limit):
        self.token_limit = token_limit

    def compress(self, messages):

        facts = []
        recent = deque(maxlen=10)
        summaries = []

        important_keywords = [
            "name",
            "goal",
            "prefer",
            "work",
            "study"
        ]

        for role, text in messages:

            if any(k in text.lower()
                   for k in important_keywords):

                facts.append(f"FACT: {text}")

            else:
                recent.append(text)

        output = facts

        output.extend(
            [f"RECENT: {msg}" for msg in recent]
        )

        current_tokens = sum(
            len(x.split()) for x in output
        )

        if current_tokens > self.token_limit:

            return output[:self.token_limit // 10]

        return output
