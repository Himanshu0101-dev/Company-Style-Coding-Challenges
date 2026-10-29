#include <iostream>
#include <vector>
using namespace std;

int longestContext(vector<long long>& tokens, long long K) {
    int left = 0;
    long long sum = 0;
    int answer = 0;

    for (int right = 0; right < tokens.size(); right++) {
        sum += tokens[right];

        while (sum > K) {
            sum -= tokens[left];
            left++;
        }

        answer = max(answer, right - left + 1);
    }

    return answer;
}

int main() {
    vector<long long> tokens = {120, 80, 150, 100, 50};
    long long K = 300;

    cout << longestContext(tokens, K);
}
