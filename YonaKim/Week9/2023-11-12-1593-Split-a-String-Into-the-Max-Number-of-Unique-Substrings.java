import java.util.ArrayList;

class Solution {
    public int maxUniqueSplit(String s) {
        String subString = "";

        ArrayList<String> subStrings = new ArrayList<String>();

        while(s.length() > 0) {
            subString += s.charAt(0);
            s = s.substring(1);
            
            if(!subStrings.contains(subString)) {
                subStrings.add(subString);
                subString = "";
            }

            //if we reach end of string and there is duplicate
        }

        return subStrings.size();
    }
}