class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded = "";
        for (auto &str : strs) {
            encoded += to_string(str.size()) + "#" + str;
        }
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> decoded;
        int i = 0;

        while (i < s.size()) {
            int j = s.find('#', i);
            int len = stoi(s.substr(i, j - i));

            i = j + 1;
            decoded.push_back(s.substr(i, len));

            i += len;
        }

        return decoded;
    }
};
