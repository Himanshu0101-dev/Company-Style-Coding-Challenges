def maximize_context_value(chunks, context_limit):
    n = len(chunks)

    dp = [[0] * (context_limit + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        tokens, importance = chunks[i - 1]

        for cap in range(context_limit + 1):
            dp[i][cap] = dp[i - 1][cap]

            if tokens <= cap:
                dp[i][cap] = max(
                    dp[i][cap],
                    dp[i - 1][cap - tokens] + importance
                )

    return dp[n][context_limit]


chunks = [
    (100, 50),
    (200, 120),
    (150, 100),
    (120, 70)
]

context_limit = 300

print(maximize_context_value(chunks, context_limit))
