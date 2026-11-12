from collections import defaultdict, deque


class RateLimiter:

    def __init__(self, k, window):
        self.k = k
        self.window = window
        self.users = defaultdict(deque)

    def process(self, user_id, timestamp):

        q = self.users[user_id]

        while q and timestamp - q[0] >= self.window:
            q.popleft()

        if len(q) < self.k:
            q.append(timestamp)
            return "ALLOW"

        return "BLOCK"


def rate_limit(k, window, requests):

    limiter = RateLimiter(k, window)

    result = []

    for user, ts in requests:
        result.append(
            limiter.process(user, ts)
        )

    return result


k = 3
window = 10

requests = [
    ("u1", 1),
    ("u1", 2),
    ("u1", 3),
    ("u1", 4),
    ("u1", 12)
]

print(rate_limit(k, window, requests))
