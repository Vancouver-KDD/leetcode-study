//2023.01.21
//[idea] - using Charactger.toLowercase(ch), Character.isLetter(ch), Character.isDigit(ch)
//input: s = "A man, a plan, a canal: Panama", output: true
//Time Complexity: O(N)
//Space Complexity: O(1)
class Solution{
    public boolean isPalindrome(String s){
        if(s == null || s.length() == 0){
            return false;
        }

        int start = 0;
        int end = s.length() -1;
        //n, a plan, a canal: Pan
        while(start < end){
            char startCh = s.charAt(start);
            char endCh = s.charAt(end);

            //if(!Character.isDigit(startCh) && !Character.isLetter(startCh)){
            if(!Character.isLetterOrDigit(startCh)){
                start++;
            //}else if(!Character.isDigit(endCh) && !Character.isLetter(endCh)){
            }else if(!Character.isLetterOrDigit(endCh)){
                end--;
            }else{
                //if(Character.isLetter(startCh) && Character.isUpperCase(startCh)){
                //    startCh = Character.toLowerCase(startCh);
                //}
                //if(Character.isLetter(endCh) && Character.isUpperCase(endCh)){
                //    endCh = Character.toLowerCase(endCh);
                //}
               // if(startCh != endCh){
               //     return false;
              //  }
              //toLowerCase 함수는 변경할 lowerCase 가 없으면 입력값 그대로 return
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
//2022.11.16
//Input: "A man, a plan, a canal: Panama" -> Output: true
//Input: "race a car" -> Output: false
//Input: " " -> Output: true
/*
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
*/
//2022.06.20
//Limitation : s is null??
//Time complexity: O(N) , Space Complexity: O(1)
/*
class Solution {
    
    public boolean isPalindrome(String s) {
        
        if(s == null || s.length() == 0){
            return false;
        }
        
        int start = 0;
        int end = s.length() -1;

        while ( start < end){
            char chLeft = s.charAt(start);
            char chRight = s.charAt(end);
            if(!Character.isLetterOrDigit(chLeft)){
                start++;
            }else if(!Character.isLetterOrDigit(chRight)){
                end--;
            }else{
                if(Character.toLowerCase(chLeft) != Character.toLowerCase(chRight)){
                    return false;
                }
                start++;
                end--;
            }
            
        }
        
        return true;
    }
}
*/
/*
class Solution {
    
    public boolean isPalindrome(String s) {
        
        int left = 0; 
        int right = s.length() -1;
        
        while(left < right){
            char leftCh = s.charAt(left);
            char rightCh = s.charAt(right);
            
            if(!Character.isLetterOrDigit(leftCh)){
                left++;
            }else if(!Character.isLetterOrDigit(rightCh)){
                right--;
            }else{
                if(Character.toLowerCase(leftCh) != Character.toLowerCase(rightCh)){
                    return false;
                }
                left++;
                right--;
            } 
        }
        return true;
    }    
}
 */   
      
    //2022.03.26 my solution
    /*
 class Solution {
    public boolean isPalindrome(String s) {
        
        // array to store the coverted alphanumeric characters
        ArrayList<Character> characters = new ArrayList<Character>();
        
        //convert 
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            //save only alphabet
            if((ch >= 'A') && ( ch <= 'Z') ){
                characters.add(Character.toLowerCase(ch));
            }else if(((ch >= 'a') && ( ch <= 'z')) || ((ch >= '0') && ( ch <= '9'))){
                characters.add(ch);   
            }
        }
        
        //System.out.println(characters.toString());
        
        int halfSize = characters.size()/2;
        
        //compare left half and right half
        for(int i = 0; i < halfSize ; i++){
            if( characters.get(i) != characters.get( characters.size() - 1 -i)){
                return false;
            }
        }
        return true;
    }
}
    */
    //Leetcode solution
    /*
class Solution {
    public boolean isPalindrome(String s) {
         StringBuilder builder = new StringBuilder();
        
        for(char ch : s.toCharArray()){
            if(Character.isLetterOrDigit(ch)){
                builder.append(Character.toLowerCase(ch));
            }
        }
        
        String convertedString = builder.toString();
        String reverseConvertedString = builder.reverse().toString();
        
        return convertedString.equals(reverseConvertedString);
     }
}
*/


