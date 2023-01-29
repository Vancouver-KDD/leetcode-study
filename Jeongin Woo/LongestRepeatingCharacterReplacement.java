import java.util.*;

public class LongestRepeatingCharacterReplacement {
	 public int characterReplacement(String s, int k) {
	       
		   Map <Character,Integer> map = new HashMap<>();
	       int start = 0 ;
	       int maxLength = 0;
	       int maxCountOfRepeatingLetter = 0;
	       
	       for(int end = 0 ; end < s.length();end++) {
	    	   
	    	   char rightChar = s.charAt(end);
	    	   map.put(rightChar, map.getOrDefault(rightChar, 0)+1);
	    	   maxCountOfRepeatingLetter = Math.max(maxCountOfRepeatingLetter,  map.get(rightChar));
	    	   if(end-start+1-maxCountOfRepeatingLetter>k)
	    	   {
	    		   char leftChar = s.charAt(start);
	    		   map.put(leftChar, map.get(leftChar)-1);
	    		   start++;
	    	   }
	    	   
	     	   maxLength = Math.max(maxLength, end-start+1);
	       }
	       
	  
	    		   
	       return maxLength;
		   
		   
	    }
}
