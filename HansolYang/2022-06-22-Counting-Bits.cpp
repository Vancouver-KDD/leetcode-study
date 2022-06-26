class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans;
        int len = 0;
        int curr = 0;
        ans.push_back(0);
        for (int i = 1; i <= n; i++) {
            if (len == 0) {
                ans.push_back(1);
                curr = 0;
                len++;
            } else if (curr == 0) {
                ans.push_back(1);
                curr++;
            } else if (curr == pow(2, len) - 1) {
                ans.push_back(len + 1);
                curr = 0;
                len++;
            } else {
                ans.push_back(ans[curr] + 1);
                curr++;
            }
        }
        
        return ans;
    }
};