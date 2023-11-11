

//2023-11-09
//Backtracking
//Time Complexity: O(4^N *N)
//      The worst-case is where the input consists of only 7s and 9s. 
//      4^N is for the combinations of N digits. And the extra N is for the
//      time on building the string. 
//      path.toString() or "".join(path). This cost O(N) time.
//Space Complexity: O(N) , N is the length of String digits
class Solution {    
    
    public List<String> letterCombinations(String digits) {
        List<String> combinations = new ArrayList<>();
        if(digits == null || digits.length() <= 0){
            return combinations;
        }
        
        String[] phone = new String[10];
        phone[2] = "abc";
        phone[3] = "def";
        phone[4] = "ghi";
        phone[5] = "jkl";
        phone[6] = "mno";
        phone[7] = "pqrs";
        phone[8] = "tuv";
        phone[9] = "wxyz";
        
        StringBuilder sb = new StringBuilder();
        backTracking(digits, 0, phone, sb, combinations);
        
        return combinations;
        
    }
    
    void backTracking(String digits, int index, String[] phone, StringBuilder letters, List<String> combinations){
        if(index >= digits.length()){
            combinations.add(letters.toString());
            return;
        }
        
        char digit = digits.charAt(index);
        String button = phone[digit - '0'];

        for(int i = 0; i < button.length(); i++){
            char ch = button.charAt(i);
            letters.append(ch);
            backTracking(digits, index+1, phone, letters, combinations);
            letters.deleteCharAt(letters.length()-1);
        }

    }
}



