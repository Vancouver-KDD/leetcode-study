class Solution {
public:
    bool isPalindrome(string s) {
        
        // remove whitespaces and convert to lowercase
        string str;
        for(auto c:s){
            if(isalnum(c)) str+=tolower(c);
        }
        
        for(int i=0; i<str.length()/2; i++){
            if(str[i]!=str[str.length()-i-1]) return false;
        }
        
        return true;
    }
};

class Solution {
public:
    bool isPalindrome(string s) {
        
        // remove whitespaces and convert to lowercase
        string str;
        for(auto c:s){
            if(isalnum(c)) str+=tolower(c);
        }
        
        // reverse str
        string rev = str;
        //strcpy(rev,str);
        for(int i=0; i<rev.length()/2; i++){
            swap(rev[i],rev[rev.length()-i-1]);
        }
        
        // compare str and reversed str
        if(rev==str) return true;
        return false;
    }
};
