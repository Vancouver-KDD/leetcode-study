class Solution {
    public int characterReplacement(String s, int k) {
        //can change it to any other uppercase Eng character -> I missed this
        int start = 0, maxCount = 0, maxLength=0;
        int len = s.length();
        char [] arr = new char[26]; //to check the number

        for(int end = 0; end<len;end++) {
            maxCount = Math.max(maxCount, ++arr[s.charAt(end)-'A']);// count 세기
            while(end-start+1-maxCount > k) {
                arr[s.charAt(start)-'A']--;
                start++;
            }
            maxLength = Math.max(maxLength, end-start+1);
        }
        return maxLength;
    }
}