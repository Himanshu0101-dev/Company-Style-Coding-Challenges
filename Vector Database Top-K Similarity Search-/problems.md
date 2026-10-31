# Problem Statement
Modern AI applications such as ChatGPT, Copilot, and AI Search engines use Vector Databases to retrieve the most relevant documents.
You are given:
A query vector Q
N document vectors
Find the Top-K most similar documents using Cosine Similarity.
Return document IDs in descending order of similarity

# input 
documents = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 1, 1],
    [7, 8, 9]
]

query = [2, 3, 4]

k = 2
# output 
[1, 3]
Document indexex
Doc 1 similarity = 0.9926
Doc 3 similarity = 0.9982

# constraints 
1 <= N <= 100000
1 <= Dimension <= 100
1 <= K <= N

# approach 
For every document:

Calculate Cosine Similarity
Cos(A,B) = A·B / (|A| × |B|)
Store similarity score
Use Max Heap
Extract Top-K documents

