from collections import defaultdict, deque

def find_rate_limit_violators(requests):
    user_requests = defaultdict(deque)
    violators = set()

    for user, timestamp in requests:
        q = user_requests[user]

        # Remove requests older than 60 seconds
        while q and timestamp - q[0] > 60:
            q.popleft()

        q.append(timestamp)

        # More than 5 requests in a 60-second window
        if len(q) > 5:
            violators.add(user)

    return sorted(list(violators))


# Example
requests = [
    ("A", 1),
    ("A", 10),
    ("A", 20),
    ("A", 30),
    ("A", 40),
    ("A", 50),
    ("B", 1),
    ("B", 70),
    ("B", 140)
]

print(find_rate_limit_violators(requests))
