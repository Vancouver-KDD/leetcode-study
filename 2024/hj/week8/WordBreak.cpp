class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> word_set(wordDict.begin(), wordDict.end());
        int str_length = s.length();
        vector<bool> dp_array(str_length + 1, false);
        dp_array[0] = true;

        for (int idx = 1; idx <= str_length; ++idx) {
            for (const string& word : word_set) {
                int word_length = word.length();
                int prev_idx = idx - word_length;
                if (prev_idx < 0) {
                    continue;
                }

                if (!dp_array[prev_idx]) {
                    continue;
                }

                if (s.substr(prev_idx, word_length) == word) {
                    dp_array[idx] = true;
                    break;
                }
            }
        }

        return dp_array[str_length];
    }
};