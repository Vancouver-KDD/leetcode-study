import java.util.*;
import java.util.regex.Pattern;
public class LC_2023_02_26_Designaddandsearchwordsdatastructure {
	
	class WordDictionary {
	    // Mapping word length as the key and the list of words as the value
	    Map<Integer, ArrayList<String>> map;
	    /** Initialize your data structure here. */
	    public WordDictionary() {
	        map = new HashMap<Integer, ArrayList<String>>();
	    }
	    
	    /** Adds a word into the data structure. */
	    public void addWord(String word) {
	        ArrayList<String> list;
	        if(map.get(word.length()) != null) list = map.get(word.length());
	        else list = new ArrayList<String>();
	        list.add(word);
	        map.put(word.length(), list);
	    }
	    
	    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
	    public boolean search(String word) {
	        ArrayList<String> list;
	        if(map.get(word.length()) != null) list = map.get(word.length());
	        else return false;
	        if(list.contains(word)) return true;
	        else {
	            Pattern regex = Pattern.compile(word);
	            for (String s:list) {
	                if (regex.matcher(s).matches()) return true;
	            }
	        }
	        return false;
	    }
	}

}
