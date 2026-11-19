# Problem Statement
Given a stream of application logs:
# Python
logs = [
"Payment Success TXN123",
"Database Timeout",
"Order Creation Failed TXN123",
"Notification Sent"
]

Build a system that:

Detects failures
Finds probable root cause
Generates incident report
Calculates severity level
Suggests fix
# expected output
Incident ID: INC001
Root Cause:
Database Timeout
Affected Flow:
Payment -> Order
Severity:
HIGH
Suggested Fix:
Retry database connection
Increase connection pool

Features
1. Log Parsing
Plain Text
INFO
WARN
ERROR
CRITICAL
2. Bug Classification
Plain Text
Database Error
API Failure
Memory Leak
Authentication Failure
Network Issue
 
3. Severity Prediction
Plain Text
CRITICAL = 100
ERROR = 80
WARN = 50
INFO = 10
