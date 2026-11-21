# Problem Statement
Given inventory data from:
Warehouse System
Website System

Find all inventory mismatches.
# Output:
ProductName WarehouseStock WebsiteStock Difference
Where:
Difference = WarehouseStock - WebsiteStock
# Example
# Input
# Warehouse
4
iPhone15 10
SamsungS24 25
AirPods 30
MacBook 15
# Website
4
iPhone15 8
SamsungS24 25
AirPods 35
MacBook 15
# Expected Output

iPhone15 10 8 2
AirPods 30 35 -5
Bonus Rule (Real Company Logic)

# Classify severity:

Difference >= 10 → CRITICAL
Difference >= 5 → HIGH
Difference >= 1 → MEDIUM

# Example:
AirPods 30 50 CRITICAL
