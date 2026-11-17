# Problem Statement
Build a system that assigns the nearest available delivery partner to incoming orders.
When a new order arrives:
Find all available drivers.
Select the nearest driver.
Assign the order.
Mark the driver as busy.
When delivery completes, the driver becomes available again.
# INPUT
 # Drivers:
D1 -> (10,20)
D2 -> (15,25)
D3 -> (30,40)

  # Orders:
O1 -> (13,22)
O2 -> (32,45)

# EXPECTED OUTPUT 
Order O1 assigned to Driver D1
Order O2 assigned to Driver D3

# CONSTRAINTS 
1 <= Drivers <= 100000
1 <= Orders <= 100000

Brute Force:
O(Drivers × Orders)
Optimized:
Priority Queue / Spatial Search
