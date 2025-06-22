class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        vector<string> output;
        string s;
        BT(0, s, digits, output);

        return output;
    }

    void BT(int i, string &s, string &digits, vector<string> &output) {
        if (i >= digits.size()) {
            output.push_back(s);
            return;
        }

        for (int j = 0; j < um[digits[i]].size(); j++) {
            s.push_back(um[digits[i]][j]);
            BT(i + 1, s, digits, output);
            s.pop_back();
        }
    }
private:
    unordered_map<char, string> um = {
        {'2', "abc"}, {'3', "def"}, {'4', "ghi"},
        {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"},
        {'8', "tuv"}, {'9', "wxyz"}
    };
};
