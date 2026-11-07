# Company Scenario
Companies like Uber, Google Maps, Smart City platforms, and Tesla Smart Parking systems receive thousands of parking requests every minute.

each parking slot has :
slotId
distanceFromGate
availableFromTime

Each vehicle request has :
vehicleId
arrivalTime

Assign the nearest available parking slot to every vehicle.
If multiple slots are available:
Minimum distance wins
If distance same → smaller slotId wins
A slot can be assigned only once.

Parking slots
[
 (1, 20, 2),
 (2, 10, 1),
 (3, 15, 3),
 (4, 10, 2)
]

vehicle arrivaals
[
 (101,1),
 (102,2),
 (103,3),
 (104,4)
]
Processing

Vehicle 101 arrives at time 1
Available slots:
Slot 2
Assign:
101 -> 2
Vehicle 102 arrives at time 2

Available:

Plain Text
Slot 1
Slot 4

Nearest:

Plain Text
Slot 4 (distance=10)

Assign:

Plain Text
102 -> 4

Vehicle 103 arrives at time 3

Available:


Slot 1
Slot 3

Nearest:
Slot 3

Assign:
103 -> 3

Vehicle 104 arrives at time 4

Available:
Slot 1
Assign:
104 -> 1
# Output

[
(101,2),
(102,4),
(103,3),
(104,1)
]
