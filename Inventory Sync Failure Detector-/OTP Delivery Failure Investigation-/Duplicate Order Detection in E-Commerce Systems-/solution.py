n = int(input())

seen = set()
duplicates = []

for _ in range(n):
    order_id, user_id, product_id, payment_id, timestamp = input().split()

    key = (user_id, product_id, payment_id)

    if key in seen:
        duplicates.append(order_id)
    else:
        seen.add(key)

for order_id in duplicates:
    print(order_id, "DUPLICATE_ORDER")
