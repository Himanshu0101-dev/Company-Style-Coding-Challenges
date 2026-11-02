from collections import Counter

class Solution:
    def topKPrompts(self, prompts, k):
        freq = Counter(prompts)

        sorted_prompts = sorted(
            freq.keys(),
            key=lambda x: (-freq[x], x)
        )

        return sorted_prompts[:k]


# Example Usage
prompts = [
    "ai",
    "code",
    "ai",
    "chatbot",
    "code",
    "ai"
]

k = 2

print(Solution().topKPrompts(prompts, k))
