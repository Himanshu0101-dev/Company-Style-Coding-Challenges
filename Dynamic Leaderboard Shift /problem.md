A gaming platform stores players' scores.
Initially, player i has score scores[i].
You are given Q updates:
[player_id, new_score]

After each update, return the number of players whose rank changed.
Ranking Rules

Higher score = better rank
 
Equal scores share the same rank.

# example
scores = [100, 90, 80]

updates = [
 [2, 110],
 [1, 70]
]

# update 1 
Player 2 : 80 → 110

Old Ranks:
100 -> 1
90  -> 2
80  -> 3

New Ranks:
110 -> 1
100 -> 2
90  -> 3

Changed Players:
all 3
# ANSWER 3

# UPDATE2 
100,90,110 → 100,70,110

Old:
110 ->1
100 ->2
90  ->3

New:
110 ->1
100 ->2
70  ->3

Changed:
Only player updated.
# ANSWER 1 
