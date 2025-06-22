class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> output;
        vector<string> v;
        BT(s, 0, v, output);
        return output;
    }

    void BT(string &s, int i, vector<string> &v, vector<vector<string>> &output) {
        if (i >= s.size()) {
            output.push_back(v);
            return;
        }

        for (int j = i; j < s.size(); j++) {
            if (isPalindrome(s, i, j)) {
                v.push_back(s.substr(i, j - i + 1));
                BT(s, j + 1, v, output);
                v.pop_back();
            }
        }
    }

    bool isPalindrome(string& s, int l, int r) {
        while (l < r) {
            if (s[l] != s[r])
                return false;
            l++;
            r--;
        }
        return true;
    }
};
