
class Solution {
    public boolean isPalindrome(String s) {
        //앞 뒤가 다 같아야 함
        //먼저, lowercase로 변화, 알파벳 아닌 거 삭제
        //start, end로 하나씩 비교하기
        StringBuilder sb = new StringBuilder();
        int len = s.length();
        s.toLowerCase();
        for(int i = 0; i<len;i++ ) {
            if(s.charAt(i) >='a' && s.charAt(i) <='z') {
                sb.append(s.charAt(i));
            }
        }
        s = sb.toString();
        len = s.length();
        int start = 0;
        
        while(start<=len) {
            if(s.charAt(start) != s.charAt(len)) {
                return false;
            }
        }
    
        return true;
    }
}