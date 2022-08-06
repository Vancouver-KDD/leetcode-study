class Solution {
public:
    int characterReplacement(string s, int k) {
        
        // empty string
        if(s.size()==0) return 0;
        
        int i=0;    // start of sliding window (i,..,j-1)
        int j=0;    // next char of window
        
        int maxCount=0, res=0;
        unordered_map<char,int> freq;
        
        // until end of string
        while(j<s.size()){
            freq[s[j]]++;   // count freq
            maxCount = max(maxCount, freq[s[j]]);
            
            // if number of other chars (that are not the highest freq) > k
            //      reduce the window and update maxCount until number <= k
            // if number <= k
            //      replace all into max freq character so all are the same character
            while(j-i-maxCount+1 > k){
                freq[s[i]]--;
                i++;
                for(auto m:freq) maxCount = max(maxCount, m.second);
            }

            // check if the adjusted window is the largest window
            res = max(res, j-i+1);
            j++;
        }
        return res;
    }
};