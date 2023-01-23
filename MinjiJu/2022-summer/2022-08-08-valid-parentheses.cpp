class Solution {
public:
    bool isValid(string s) {

        stack<char> p;
        
        for(int i=0; i<s.length(); i++){
            if(s[i]=='(' || s[i]=='{' || s[i]=='['){
                p.push(s[i]);
            }
            else{
                if(p.empty()) return false;
                if(p.top()=='(' && s[i]!=')' || p.top()=='{' && s[i]!='}' || p.top()=='[' && s[i]!=']') return false;
                p.pop();
            }
        }
        return p.empty() ? true : false;
    }
};