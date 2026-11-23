# Problem

In fintech/e-commerce companies, payments and orders are stored in different systems. 
Sometimes an order is marked PAID but no payment record exists, or a payment exists without an order update
# given
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
# find
Orders with no payment.
Payments with no order.
Orders where amount mismatch exists.

# expected output 
Missing Payments:
ORD3

Unknown Payments:
ORD4

Amount Mismatches:
ORD2 (Order=1000, Payment=900)
