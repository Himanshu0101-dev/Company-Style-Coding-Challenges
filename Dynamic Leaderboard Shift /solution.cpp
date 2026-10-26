#include <bits/stdc++.h>
using namespace std;

vector<int> rankShift(vector<int>& scores,
                      vector<vector<int>>& updates)
{
    int n = scores.size();

    vector<int> answer;

    for(auto &q : updates)
    {
        int player = q[0];
        int newScore = q[1];

        vector<int> oldScores = scores;

        auto getRanks = vector<int>& arr
        {
            int n = arr.size();

            vector<pair<int,int>> temp;

            for(int i=0;i<n;i++)
            {
                temp.push_back({-arr[i], i});
            }

            sort(temp.begin(), temp.end());

            vector<int> rank(n);

            int currentRank = 1;

            rank[temp[0].second] = 1;

            for(int i=1;i<n;i++)
            {
                if(-temp[i].first != -temp[i-1].first)
                    currentRank = i + 1;

                rank[temp[i].second] = currentRank;
            }

            return rank;
        };

        vector<int> oldRank = getRanks(oldScores);

        scores[player] = newScore;

        vector<int> newRank = getRanks(scores);

        int changed = 0;

        for(int i=0;i<n;i++)
        {
            if(oldRank[i] != newRank[i])
                changed++;
        }

        answer.push_back(changed);
    }

    return answer;
}
