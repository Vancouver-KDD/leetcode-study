package week1;
import java.util.*;

/*
 * Week 1: Array & Hashing
 * https://leetcode.com/problems/group-anagrams/
 */
class Solution {
    public static List<List<String>> groupAnagrams(String[] strs) {
        // sort char in string
        // store map for grouping (key=sorted string, value = original string)
        Map<String, List<String>> groups = new HashMap<>();

        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sortedStr = new String(chars);

            groups.putIfAbsent(sortedStr, new ArrayList<>());
            groups.get(sortedStr).add(str);
        }

        return new ArrayList(groups.values());
    }

    public static void main(String[] args) {
        String[] strs = {"eat","tea","tan","ate","nat","bat"};
        groupAnagrams(strs);
    }
}