# Real Company Scenario
Companies like:
Amazon
Flipkart
Blinkit
Myntra
Swiggy Instamart
sometimes face this issue:
Customer clicks "Place Order" multiple times because the app hangs or network is slow.
# result :
Order O101 Created
Order O102 Created
Order O103 Created
for the same payment.
This causes:
Double charges
Duplicate deliveries
Refund requests
Customer complaints

# Problem Statement
Given order logs:
orderId userId productId paymentId timestamp
Identify duplicate orders.
A duplicate order is one where:

Same userId
Same productId
Same paymentId
appears more than once.
Report all duplicate orderIds except the first valid order.

# example input 
6
O101 U1 P10 PAY100 1000
O102 U2 P15 PAY200 1010
O103 U1 P10 PAY100 1020
O104 U3 P20 PAY300 1030
O105 U2 P15 PAY200 1050
O106 U1 P11 PAY101 1060

# expected output 
O103 DUPLICATE_ORDER
O105 DUPLICATE_ORDER
