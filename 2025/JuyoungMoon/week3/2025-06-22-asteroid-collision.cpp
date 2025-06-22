// Author: Juyoung Moon

// KDD LeetCode Study Week 3: Stack.
// https://github.com/juyomo/leetcode-study

// LeetCode #735.
// https://leetcode.com/problems/asteroid-collision/

class Solution {
public:
    bool isValid(string s) {
        int size = s.length();
        if (size % 2 != 0) {
            return false;
        }
        stack<char> stk;

        for (int i = 0; i < size; i++) {
            char curr = s[i];
            switch (curr) {
                case '[':
                    stk.push(']');
                    break;
                case '{':
                    stk.push('}');
                    break;
                case '(':
                    stk.push(')');
                    break;
                default:
                    if (stk.empty() || stk.top() != curr) {
                        return false;
                    }
                    stk.pop();
            }
        }

        return stk.empty();
    }
};