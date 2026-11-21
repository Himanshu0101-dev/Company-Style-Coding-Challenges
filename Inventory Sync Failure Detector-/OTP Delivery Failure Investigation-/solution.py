n = int(input())

events = {}

for _ in range(n):
    request_id, event = input().split()

    if request_id not in events:
        events[request_id] = set()

    events[request_id].add(event)

result = []

for request_id, ev in events.items():

    if "OTP_GENERATED" not in ev:
        result.append((request_id, "OTP_SERVICE_FAILURE"))

    elif "SMS_SENT" not in ev:
        result.append((request_id, "SMS_GATEWAY_FAILURE"))

    elif "SMS_DELIVERED" not in ev:
        result.append((request_id, "SMS_DELIVERY_FAILURE"))

result.sort()

for request_id, issue in result:
    print(request_id, issue)
