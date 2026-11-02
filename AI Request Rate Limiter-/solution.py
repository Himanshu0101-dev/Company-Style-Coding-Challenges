from collections import defaultdict, deque

class Solution:
    def rateLimitedUsers(self, requests, k, window):
        user_windows = defaultdict(deque)
        violators = set()

        for timestamp, user in requests:
            dq = user_windows[user]

            while dq and timestamp - dq[0] >= window:
                dq.popleft()

            dq.append(timestamp)

            if len(dq) > k:
                violators.add(user)

        return sorted(list(violators))


# Example Usage
requests = [
    [1, "A"],
    [2, "A"],
    [3, "A"],
    [5, "B"],
    [6, "B"],
    [7, "B"]
]

k = 2
window = 3

print(Solution().rateLimitedUsers(requests, k, window))
