class Solution {
public:
    bool isValid(string s) {
        vector<char> opens;
        
        for (int i = 0; i < s.size(); i++) {
            cout << s.at(i) << endl;
            char curr = s.at(i);
            if (curr == '{' || curr == '[' || curr == '(') {
                opens.push_back(curr);
            } else {
                if (opens.size() == 0 || !matchPair(opens.back(), curr)) {
                    return false;
                }
                else {
                    opens.pop_back();
                }
            }
        }
        
        return opens.size() == 0;
    }
    
    bool matchPair(char c1, char c2) {
            return (c1 == '{' && c2 == '}') || (c1 == '[' && c2 == ']') || 
                (c1 == '(' && c2 == ')');
    }
};