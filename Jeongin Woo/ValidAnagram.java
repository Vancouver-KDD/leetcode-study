import java.util.Arrays;

public class ValidAnagram {
	
	    public boolean isAnagram(String s, String t) {

	        char stringS [] = s.toCharArray();
	        char stringT [] = t.toCharArray();

	        if(stringS.length != stringT.length)
	        return false;

	        Arrays.sort(stringS);
	        Arrays.sort(stringT);
	        for(int i =0;i < stringS.length;i++){
	            if(stringS[i] != stringT[i]){
	                return false;
	            }
	        }
	        return true;
	    }
	        
}
