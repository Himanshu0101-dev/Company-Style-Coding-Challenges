# Problem Statement
You are working on an AI customer-support chatbot that uses a RAG (Retrieval-Augmented Generation) pipeline.
A bug was reported:
The chatbot sometimes answers questions even when no relevant document was retrieved.
Engineers want to identify potentially hallucinated responses.
A response is considered hallucinated if:
Retrieval confidence < 0.70
AND the chatbot still generated an answer

Return all query IDs that are potentially hallucinated.

Input
Python
logs = [
("Q101", 0.92, True),
("Q102", 0.45, True),
("Q103", 0.81, True),
("Q104", 0.32, True),
("Q105", 0.65, False)
]

Where:

Plain Text
(query_id, confidence_score, answer_generated)
Expected Output
Python
["Q102", "Q104"]
