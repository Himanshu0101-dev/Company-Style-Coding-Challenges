def detect_hallucinations(logs):
    result = []

    for query_id, confidence, answered in logs:
        if confidence < 0.70 and answered:
            result.append(query_id)

    return result


logs = [
    ("Q101", 0.92, True),
    ("Q102", 0.45, True),
    ("Q103", 0.81, True),
    ("Q104", 0.32, True),
    ("Q105", 0.65, False)
]

print(detect_hallucinations(logs))
