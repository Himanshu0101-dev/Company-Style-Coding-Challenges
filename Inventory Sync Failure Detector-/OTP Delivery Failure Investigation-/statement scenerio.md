# Real Company Scenario
Companies:

Paytm
PhonePe
Google Pay
Banking Apps
IRCTC
Flipkart

# A customer says:
"I clicked Send OTP 5 times but never received it."
Support engineers must determine whether:
OTP Request reached the server
OTP was generated
SMS Gateway received it
SMS was delivered

# log format 
requestId event
# events
OTP_REQUESTED
OTP_GENERATED
SMS_SENT
SMS_DELIVERED

# example input 
10

R101 OTP_REQUESTED
R101 OTP_GENERATED
R101 SMS_SENT
R101 SMS_DELIVERED

R102 OTP_REQUESTED
R102 OTP_GENERATED
R102 SMS_SENT

R103 OTP_REQUESTED
R103 OTP_GENERATED

R104 OTP_REQUESTED
