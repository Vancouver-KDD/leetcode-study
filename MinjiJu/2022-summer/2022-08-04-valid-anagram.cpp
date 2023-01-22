class Solution {
public:
    bool isAnagram(string s, string t) {

        // if strings are different length return false
        if(s.length()!=t.length()){return false;}
        
        // sort both strings alphabetically
        sort(s.begin(),s.end());
        sort(t.begin(),t.end());
        
        // compare sorted strings (if equal then true)
        if(s!=t){return false;}
        return true;
    }
};