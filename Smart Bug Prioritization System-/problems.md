# Problem Statement
In large companies, hundreds of bugs are reported daily. QA teams need a system that automatically prioritizes bugs based on severity, customer impact, and occurrence frequency.
Build a system that processes bug reports and returns them sorted by priority.
# Input
bugId severity impactedUsers occurrences
# Severity Mapping:
CRITICAL = 5
HIGH = 4
MEDIUM = 3
LOW = 2
TRIVIAL = 1
# Priority Score:
priorityScore =
(severityValue * 100)
+ (impactedUsers * 5)
+ (occurrences * 2)
Sort by:
Higher priorityScore
If tie → More impacted users
If tie → Smaller bugId
# Example
# Input:

4
 
101 HIGH 50 20
102 CRITICAL 15 30
103 MEDIUM 100 10
104 HIGH 50 25

# Output:
102
104
101
103
