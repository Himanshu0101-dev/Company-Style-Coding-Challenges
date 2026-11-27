# Problem Statement
You are working as a Software Engineer in an e-commerce company.
Customers make payments through multiple gateways (Razorpay, PayU, Stripe, etc.). Sometimes the payment gateway reports a transaction as SUCCESS, but due to network issues, the company's database doesn't record the order.
This creates a mismatch:
Gateway Transaction → SUCCESS
Internal Order → MISSING
Finance teams run reconciliation jobs daily to identify such failures and recover lost orders or refund customers.
Given:
A list of successful payment transaction IDs from the gateway.
A list of transaction IDs recorded in the company's order database.
Find all transaction IDs that are present in the gateway data but missing in the database.

# input
gateway = [101,102,103,104,105,106]
database = [101,103,104,106]
# Output

[102,105]
