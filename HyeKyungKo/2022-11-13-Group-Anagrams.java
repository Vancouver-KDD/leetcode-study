//Limitation : strs size?  if size is zero, return zeor size array. 
//Input: strs = ["eat","tea","tan","ate","nat","bat"] ---> Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
//Input: strs = [""] ---> Output: [[""]]
//Input: strs = ["a"] ---> Output: [["a"]]

//Leetcode Solution#1 -- uning 'Character Array sorting'
//Time Complexity: O(N*KlogK), Space Complexity: O(N*K) <--- 왜 Space Complexity 가 N*K 인지 잘 모르겠다. -> 단순히 배열자체의 length 만 따진게 아니라 String개수 N 에다가 각각의 String 크기 평균치 K 도 계산에 넣은듯
/*
class Solution{
    public List<List<String>> groupAnagrams(String[] strs){
        HashMap<String, List<String>> groupMap = new HashMap<>();

        if(strs == null || strs.length == 0){
            return new ArrayList<List<String>>();
        }

        for(String str: strs){
            char[] chArr = str.toCharArray();
            Arrays.sort(chArr);
            String sortedStr = new String(chArr);

            if(!groupMap.containsKey(sortedStr)){
                groupMap.put(sortedStr, new ArrayList<>()); 
            }
           groupMap.get(sortedStr).add(str);         
        }

        return new ArrayList(groupMap.values());
    }
}
*/
//Time complexity : O(N*K)
//Space Complexity: O(N*K)
class Solution{
    public List<List<String>> groupAnagrams(String[] strs){
        HashMap<String, List<String>> groupMap = new HashMap<>();

        if(strs == null || strs.length == 0){
            return new ArrayList<List<String>>();
        }

        int[] alphabetArr = new int[26];

        for(String str : strs){
            Arrays.fill(alphabetArr, 0);

            for(int i = 0; i < str.length(); i++){
                alphabetArr[str.charAt(i) - 'a']++;
            }

            StringBuilder key = new StringBuilder();
            for(int i = 0; i < alphabetArr.length ; i++){
                key.append(alphabetArr[i]);
                key.append('#');
            }

            if(!groupMap.containsKey(key.toString())){
                groupMap.put(key.toString(), new ArrayList<>());
            }
            groupMap.get(key.toString()).add(str);
        }

        return new ArrayList(groupMap.values());
    }
}
/*
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> groupMap = new HashMap<>();
        
        for(int i = 0; i < strs.length; i++){
            char[] letters = strs[i].toCharArray();
            Arrays.sort(letters);
            
            String key = String.valueOf(letters); //new String(letters); 와의 차이가 뭐지???
            
            groupMap.putIfAbsent(key, new ArrayList<>()); //여기에다가 new ArrayList<String>() 이렇게 안해도 되나???
            groupMap.get(key).add(strs[i]);
        }
        
        return new ArrayList<>(groupMap.values());
    }
}
*/


//Leetcode Solution#2 -- uning 'Character Counts'
//Time Complexity: O(N*K + N*A) <-- K is max string size, A is 26
//Space Complexity: O(N*K)
/*
class Solution {
    final int ALPHABET_NUM = 26;
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> groupMap = new HashMap<>();
        int[] alphabet = new int[ALPHABET_NUM];
        
        for(int i = 0; i < strs.length; i++){
            Arrays.fill(alphabet, 0);
           
            for(int j = 0; j < strs[i].length(); j++){
                alphabet[strs[i].charAt(j) - 'a']++;
            }
            
            StringBuilder key = new StringBuilder();
            for(int j = 0; j < ALPHABET_NUM; j++){
                key.append(alphabet[j]);
                key.append('#');
            }
            
            groupMap.putIfAbsent(key.toString(), new ArrayList<String>());
            groupMap.get(key.toString()).add(strs[i]);
        }
        
        return new ArrayList<List<String>>(groupMap.values());
    }
}
*/

//My Solution 2022.05.14
//Time complexity: O() , Space complexity: O()
/*
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if(strs == null || strs.length == 0){
            return null;
        } 
        
        String[] sortedStr = new String[strs.length];
        inputSorting(strs, sortedStr);
        
        List<List<Integer>> output = new ArrayList<List<Integer>>();
        List<Integer> first = new ArrayList<Integer>();
        first.add(0);
        output.add(first);
        
        
        for(int i = 1; i < strs.length; i++){
            int count = 0;
            while(count < output.size()){
                List<Integer> indexList = output.get(count);
                int index = indexList.get(0);
                if(sortedStr[index].compareTo(sortedStr[i])==0){
                    indexList.add(i);
                    break;
                }                
                count++;
            }
            if(count == output.size()){
                List<Integer> newList = new ArrayList<Integer>();
                newList.add(i);
                output.add(newList);
            }
        }
        
        List<List<String>> anagramsList = new ArrayList<List<String>>();
        for(int i = 0; i < output.size(); i++){
            List<String> strList = new ArrayList<String>();
            List<Integer> indexList = output.get(i);
            for(int j = 0; j < indexList.size(); j++){
                strList.add(strs[indexList.get(j)]);
            }
            anagramsList.add(strList);
        }
        
        return anagramsList;
    }
    
    private void inputSorting(String[] source, String[] destination){
        
        for(int i = 0; i < source.length; i++){
            char[] letters = source[i].toCharArray();
            Arrays.sort(letters);
            destination[i] = new String(letters);
        }
    }
}
*/