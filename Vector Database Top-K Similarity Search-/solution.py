import heapq
import math

def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))

    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))

    if norm_a == 0 or norm_b == 0:
        return 0

    return dot / (norm_a * norm_b)


def top_k_documents(documents, query, k):

    heap = []

    for idx, doc in enumerate(documents):

        sim = cosine_similarity(doc, query)

        heapq.heappush(heap, (-sim, idx))

    result = []

    for _ in range(k):
        similarity, doc_id = heapq.heappop(heap)
        result.append(doc_id)

    return result


documents = [
    [1,2,3],
    [4,5,6],
    [1,1,1],
    [7,8,9]
]

query = [2,3,4]
k = 2

print(top_k_documents(documents, query, k))
