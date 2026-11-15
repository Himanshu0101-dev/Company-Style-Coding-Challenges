from collections import deque

def longestStableRollout(successRate, k):
    maxdq = deque()
    mindq = deque()

    left = 0
    answer = 0

    for right in range(len(successRate)):

        while maxdq and successRate[maxdq[-1]] <= successRate[right]:
            maxdq.pop()

        while mindq and successRate[mindq[-1]] >= successRate[right]:
            mindq.pop()

        maxdq.append(right)
        mindq.append(right)

        while successRate[maxdq[0]] - successRate[mindq[0]] > k:

            if maxdq[0] == left:
                maxdq.popleft()

            if mindq[0] == left:
                mindq.popleft()

            left += 1

        answer = max(answer, right - left + 1)

    return answer


print(longestStableRollout([85,88,90,84,87,95], 6))
