// TC O(n^2)
class Solution {
public:
    string longestPalindrome(string s) {
        
        int st=0, ed=0, mx=INT_MIN;
        if(s.length()<=1) return s;
        
        // odd palindrome length (central element exists)
        for(int i=0; i<s.length()-1; i++){
            int l=i, r=i;
            while(l>=0 && r<s.length() && s[l]==s[r]){
                l--; r++;
            }
            int len = r-l-1;
            if(len>mx){
                mx = len;
                st = l+1;
                ed = r-1;
            }
        }
        // even palindrome length (no central element)
        for(int i=0; i<s.length()-1; i++){
            int l=i, r=i+1;
            while(l>=0 && r<s.length() && s[l]==s[r]){
                l--; r++;
            }
            int len = r-l-1;
            if(len>mx){
                mx = len;
                st = l+1;
                ed = r-1;
            }
        }
        // return substring that starts at st of mx length
        return s.substr(st,mx);
    }
};