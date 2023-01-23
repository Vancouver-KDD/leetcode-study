import java.util.*;

public class GroupAnagram {
	 public List<List<String>> groupAnagrams(String[] strs) {
	       List<List<String>> groupAnagram = new ArrayList<>();
	       HashMap<String,List<String>>map = new HashMap<>();

	       for( String ele : strs){
	           char [] character = ele.toCharArray();
	           Arrays.sort(character);
	           String sortedString = new String(character);
	           if(!map.containsKey(sortedString)){
	               map.put(sortedString,new ArrayList<>());
	           }
	           map.get(sortedString).add(ele);
	       } 
	       groupAnagram.addAll(map.values());
	       return groupAnagram;
	       
	    }
}
