class DSU {
public:
    vector<int> parent, sz;

    DSU(int n) {
        parent.resize(n);
        sz.resize(n, 1);

        for (int i = 0; i < n; i++)
            parent[i] = i;
    }

    int find(int x) {
        if (parent[x] == x)
            return x;

        return parent[x] = find(parent[x]);
    }

    void unite(int a, int b) {
        a = find(a);
        b = find(b);

        if (a == b) return;

        if (sz[a] < sz[b])
            swap(a, b);

        parent[b] = a;
        sz[a] += sz[b];
    }
};

class Solution {
public:
    int largestConnectedGroup(vector<int>& ids) {

        int n = ids.size();

        DSU dsu(n);

        vector<int> digitOwner(10, -1);

        for (int i = 0; i < n; i++) {

            int x = ids[i];

            vector<int> digits;

            if (x == 0)
                digits.push_back(0);

            while (x) {
                digits.push_back(x % 10);
                x /= 10;
            }

            sort(digits.begin(), digits.end());
            digits.erase(unique(digits.begin(),
                                digits.end()),
                                digits.end());

            for (int d : digits) {

                if (digitOwner[d] == -1)
                    digitOwner[d] = i;
                else
                    dsu.unite(i, digitOwner[d]);
            }
        }

        int ans = 1;

        for (int i = 0; i < n; i++)
            ans = max(ans, dsu.sz[dsu.find(i)]);

        return ans;
    }
};
