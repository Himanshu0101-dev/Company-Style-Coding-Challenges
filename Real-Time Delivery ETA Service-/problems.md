# Problem
A company receives live updates from delivery agents.
Build a service that:
Tracks delivery partner location
Calculates ETA to customer
Updates ETA whenever driver moves
Detects delays
Sends alerts if ETA increases too much
# example 
Order #101
Restaurant -> Customer = 10 km
Driver Position Updates:
Minute 0 : 2 km away
Minute 2 : 1.5 km away
Minute 4 : 1 km away
Minute 8 : 1.2 km away   (traffic)
ETA changed:
5 min -> 7 min
Trigger Alert:
"Order delayed due to traffic"
# what companies expect 
OrderManager
DriverTracker
ETAEngine
NotificationService
# Features
✅ Add Order
✅ Update Driver Location
✅ Calculate ETA
✅ Delay Detection
✅ Alert Generation

# Advanced Version

10000 drivers
50000 active orders
 
Need ETA in O(log n) time
