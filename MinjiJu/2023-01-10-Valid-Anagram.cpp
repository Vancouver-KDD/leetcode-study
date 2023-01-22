//---------------------------------------
// Using sort and compare
//---------------------------------------
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

// same stuff
class Solution {
public:
    bool isAnagram(string s, string t) {
        
        // base case
        if(s.length()!=t.length()) return false;

        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        if(s.compare(t)!=0) return false;
        return true;
    }
};

//---------------------------------------
// Using unordered_map
//---------------------------------------
class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if(s.length() != t.length()) return false;

        unordered_map<char,int> mp;
        
        for(auto c : s){
            mp[c]++;
        }

        for(auto c : t){
            mp[c]--;
            if(mp[c] < 0) return false;
        }        
        return true;
    }
};