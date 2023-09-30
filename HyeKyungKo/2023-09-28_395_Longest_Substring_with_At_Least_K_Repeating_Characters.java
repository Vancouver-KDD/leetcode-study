
//2023-09-26
//Solution: sliding window - 그런데 unique한 alpahbet 의 개수를 fix 한 상태에서 풀수 있는 솔루션이라서 
// 허용가능한 unique한 alpahbet 이 1개일때부터 max 개까지 for 문 돌면서 매번 sliding window 방법적용
//
//Time Complexity: O(N) , 정확하게는 O(N * maxUnique)인데 maxUnique 는 최대경우가 26으로 fix 된 값으로 생략가능
//Space Complexity: O(1) 알파벳 체크하는 사이즈 26으로 fix 된 배열만 잡고 쓰므로.
class Solution {
    public int longestSubstring(String s, int k) {
        if(s == null || s.length() <= 0) {
            return 0;
        }
        
        int maxUnique = numberOfUniqueChar(s);
        int[] repeating = new int[26];
        int longest = 0;      
        //"aaabb", k:3 
        //numUnique:1
        //start:0->1
        //end:0->1->2->3
        //countUnique:0->1->2
        //countKOrMore:0->1->0
        //repeating:a[3]b[1]
        //longest: 0->1
        for(int numUnique = 1; numUnique <= maxUnique; numUnique++){
            Arrays.fill(repeating, 0);
            
            int start = 0;
            int end = 0;
            int countUnique = 0;
            int countKOrMore = 0;
            int idx = 0;
            while(end < s.length()){
                if(countUnique <= numUnique){
                    idx = s.charAt(end) - 'a';
                    if(repeating[idx] == 0){
                        countUnique++;
                    }
                    repeating[idx]++;
                    if(repeating[idx] == k){
                        countKOrMore++;
                    } 
                    end++;
                }else{
                    idx = s.charAt(start) - 'a';
                    if(repeating[idx] == k){
                        countKOrMore--;
                    }
                    repeating[idx]--;
                    if(repeating[idx] == 0){
                        countUnique--;
                    }
                    start++;
                }
                if(countUnique == numUnique && countKOrMore == numUnique){
                    longest = Math.max(longest, end - start);
                }
            }
        }
        return longest;
    }
    
    int numberOfUniqueChar(String s){
        Set<Character> charSet = new HashSet<>();
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(!charSet.contains(ch)){
                charSet.add(ch);
            }
        }
        
        return charSet.size();
    }
}

//brute force -이 방법도 submit 하면 Accepted 됨. 
//idea : for 문 2번 돌면서 [i]부터[j]까지 범위에 있는 character 들이 같은alpahbet 이 k개 이상인지 check
//Time Complexity: O(N^2) , 같은 알파벳이 k개 이상인지 체크하는것은 늘 26개 체크해서 계산에서 제외
//Space Complexity: O(1) , 알파벳 체크하는 사이즈 26으로 fix 된 배열만 잡고 쓰므로. 
/*
class Solution {
    public int longestSubstring(String s, int k) {
        
        if(s == null || s.length() <= 0){
            return 0;
        }
        
        int longest = 0;

        //Input: s = "aaabb", k = 3

        //end:a, a, a
        //lognest:3
        for(int start = 0; start < s.length(); start++){
            int[] repeat = new int[26];
            for(int end = start; end < s.length(); end++){
                char ch = s.charAt(end);
                repeat[ch - 'a']++;
                if(kRepeating(repeat, k)){
                    longest = Math.max(longest, end - start +1);
                }
            }
        }
        return longest;
    }
    
    boolean kRepeating(int[] repeating, int k){
        for(int i = 0; i < repeating.length; i++){
            if(repeating[i] > 0 && repeating[i] < k){
                return false;
            }
        }
        return true;
    }
}
*/