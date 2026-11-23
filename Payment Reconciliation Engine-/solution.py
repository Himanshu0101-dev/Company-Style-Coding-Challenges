orders = [
    ("ORD1", 500),
    ("ORD2", 1000),
    ("ORD3", 750)
]

payments = [
    ("ORD1", 500),
    ("ORD2", 900),
    ("ORD4", 300)
]

order_map = dict(orders)
payment_map = dict(payments)

missing_payments = []
unknown_payments = []
mismatches = []

for order_id, amount in order_map.items():
    if order_id not in payment_map:
        missing_payments.append(order_id)
    elif payment_map[order_id] != amount:
        mismatches.append(
            (order_id, amount, payment_map[order_id])
        )

for payment_id in payment_map:
    if payment_id not in order_map:
        unknown_payments.append(payment_id)

print("Missing Payments:")
for x in missing_payments:
    print(x)

print("\nUnknown Payments:")
for x in unknown_payments:
    print(x)

print("\nAmount Mismatches:")
for order_id, order_amt, payment_amt in mismatches:
    print(
        f"{order_id} (Order={order_amt}, Payment={payment_amt})"
    )
