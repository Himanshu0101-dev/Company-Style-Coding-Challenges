from collections import defaultdict


def aggregate_notifications(notifications, k):
    groups = defaultdict(list)

    # Group timestamps by (userId, appName)
    for user_id, app_name, timestamp in notifications:
        groups[(user_id, app_name)].append(timestamp)

    result = {}

    for (user_id, app_name), timestamps in groups.items():
        timestamps.sort()

        batches = 1  # First batch always exists

        for i in range(1, len(timestamps)):
            if timestamps[i] - timestamps[i - 1] > k:
                batches += 1

        result[(user_id, app_name)] = batches

    return result


# Example Usage
notifications = [
    ("u1", "Instagram", 100),
    ("u1", "Instagram", 105),
    ("u1", "Instagram", 108),
    ("u1", "WhatsApp", 110),
    ("u1", "Instagram", 130)
]

k = 10

result = aggregate_notifications(notifications, k)

for (user, app), batches in result.items():
    print(f"{user} -> {app}: {batches} batches")
