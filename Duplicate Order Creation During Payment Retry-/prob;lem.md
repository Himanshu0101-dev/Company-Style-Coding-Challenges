# Problem Statement
You are working as a Software Engineer in an e-commerce company such as Amazon, Flipkart, or Blinkit.
Customers occasionally report receiving duplicate orders even though they intended to purchase an item only once.
After investigating, the engineering team discovers the following scenario:
A customer clicks "Pay Now".
Due to network latency or payment gateway delays, the response takes longer than expected.
The customer assumes the payment failed and clicks the payment button again.
The system unintentionally creates multiple orders for the same purchase.
To identify such cases, you are given a list of order creation logs. Each log contains:

(user_id, order_amount, timestamp)

A pair of orders is considered a potential duplicate if:

Both orders belong to the same user.
Both orders have the same order amount.
The difference between their timestamps is at most 30 seconds.

Return all suspicious duplicate order pairs.

# Example
# Input
# Python
orders = [
("U1", 500, 100),
("U1", 500, 105),
("U2", 800, 200),
("U3", 300, 250),
("U3", 300, 260)
]
# Output
# Python
[
("U1", 100, 105),
("U3", 250, 260)
]
# Explanation
User U1 placed two orders of amount 500 within 5 seconds, making them a potential duplicate.
User U3 placed two orders of amount 300 within 10 seconds, making them a potential duplicate.
User U2 has only one order and therefore cannot have a duplicate.
# Constraints

1 ≤ number of orders ≤ 100000
1 ≤ order_amount ≤ 10^6
0 ≤ timestamp ≤ 10^9
