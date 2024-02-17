https://leetcode.com/problems/repeated-dna-sequences/description/

class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        Set<String> subStrings = new HashSet<>();
        Set<String> results = new HashSet<>();
        int start = 0;

        for(int end = 9; end < s.length(); end++){
            if(end - start +1 == 10) {
                String result = s.substring(start, start+10);
                if(subStrings.contains(result)) {
                    results.add(result);
                }
                subStrings.add(s.substring(start, start+10));
                start++;
            }
        }
        return new ArrayList<>(results);
    }
}