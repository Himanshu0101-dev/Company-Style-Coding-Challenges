# Problem Statement
Your company is building an LLM-powered chatbot.
For each AI response, you receive:
response_id
confidence_score
fact_check_score
user_feedback_score
A response is considered a potential hallucination if:
confidence_score > 80
AND
fact_check_score < 50
Additionally, multiple suspicious responses occurring within a short period should be grouped into one incident.
For each response, determine:
SAFE
HALLUCINATION
and return the total number of incidents.
# INPUT 
[
(101,90,30,70),
(102,95,20,65),
(103,60,90,80),
(104,92,40,70)
]
# output
Response 101 -> HALLUCINATION
Response 102 -> HALLUCINATION
Response 103 -> SAFE
Response 104 -> HALLUCINATION

Incidents = 2
