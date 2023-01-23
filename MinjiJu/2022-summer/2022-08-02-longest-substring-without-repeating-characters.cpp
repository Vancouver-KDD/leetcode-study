class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        unordered_map<char,int> freq;
        int left=0, right=0, res=0;
        
        while(right<s.length()){
            
            // map character freq
            freq[s[right]]++;
            
            // if character already exists
            while(freq[s[right]] > 1){
                freq[s[left]]--;    // decrement character count
                left++;             // start from next character
            }            
            res = max(res, right-left+1);   // length of longest substring
            right++;
        }        
        return res;
    }
};