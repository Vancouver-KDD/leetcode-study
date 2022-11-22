//2022.11.16
//Input: "A man, a plan, a canal: Panama" -> Output: true
//Input: "race a car" -> Output: false
//Input: " " -> Output: true
class Solution{
    
    public boolean isPalindrome(String s){

        if(s == null || s.length() == 0){
            return false;
        }

        int start = 0;
        int end = s.length() - 1;

        while(start < end){
            char startCh = s.charAt(start);
            char endCh = s.charAt(end);
            if(!Character.isLetterOrDigit(startCh)){
                start++;
            }else if(!Character.isLetterOrDigit(endCh)){
                end--;
            }else{ // Both 'startCh' and 'endCh' are 'letter or digit'. 
                if(Character.toLowerCase(startCh) != Character.toLowerCase(endCh)){
                    return false;
                }
                start++;
                end--;
            }
        }

        return true;
    }
}
