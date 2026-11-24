from collections import defaultdict

def detect_fraud(accounts):
    phone_map = defaultdict(list)
    device_map = defaultdict(list)
    ip_map = defaultdict(list)

    suspicious = set()

    for user, phone, device, ip in accounts:
        phone_map[phone].append(user)
        device_map[device].append(user)
        ip_map[ip].append(user)

    for users in phone_map.values():
        if len(users) > 1:
            suspicious.update(users)

    for users in device_map.values():
        if len(users) > 1:
            suspicious.update(users)

    for users in ip_map.values():
        if len(users) > 3:
            suspicious.update(users)

    return sorted(suspicious)

accounts = [
    ("u1", "9876", "dev1", "1.1.1.1"),
    ("u2", "9876", "dev2", "1.1.1.2"),
    ("u3", "1234", "dev1", "1.1.1.3"),
    ("u4", "5678", "dev1", "1.1.1.4")
]

print(detect_fraud(accounts))
