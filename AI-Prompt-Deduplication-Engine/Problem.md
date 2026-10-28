# Problem Statement
Modern AI chat systems store millions of prompts. Many prompts are almost identical.
Given an array of prompts, determine the largest group of prompts that become identical after:
Converting all characters to lowercase.
Removing spaces.
Sorting the characters.
Return the size of the largest group.

# EXAMPLE
Input:
[
 "Open AI",
 "AI Open",
 "Hello",
 "Olelh",
 "Jarvis"
]

Output:
2

# EXPLANATION
"Open AI" -> "aeinoop"
"AI Open" -> "aeinoop"

"Hello" -> "ehllo"
"Olelh" -> "ehllo"

# CONSTRAINTS
1 <= n <= 100000
1 <= prompt length <= 100
