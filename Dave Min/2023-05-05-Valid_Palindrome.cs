
public class Solution {
    public bool IsPalindrome(string s) {
        int l=0;
        int r=s.Length-1;

        while(l<r){
            while(l<r && !Char.IsLetterOrDigit(s[l])){
                l++;
            }
            while(l<r && !Char.IsLetterOrDigit(s[r])){
                r--;
            }

            if(!Char.ToUpper(s[l]).Equals(Char.ToUpper(s[r]))) return false;
            l++;
            r--;
        }
        return true;
    }
}

//Time complexity: O(N)
//Space complexity: O(1)
