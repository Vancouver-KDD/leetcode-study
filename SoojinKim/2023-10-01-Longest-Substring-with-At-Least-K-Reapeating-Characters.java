class Solution {
    public int longestSubstring(String s, int k) {
        int [] alpha = new int[26];
        char [] c = s.toCharArray();
        for(int i=0; i<c.length; i++){
            int index = c[i]-'a';
            alpha[index]++;
        }
        boolean vaild = true;
        int max = 0;
        int start = 0;
        for(int end=0; end<c.length; end++){
            int index = c[end]-'a';
            if(alpha[index]<k && alpha[index]>0){
                String str = s.substring(start,end);
                max = Math.max(max,longestSubstring(str,k));
                start = end+1;
                vaild = false;
            }
        }
        if(vaild){
            return s.length();
        }else{
            return Math.max(max, longestSubstring(s.substring(start),k));
        }
    }
}