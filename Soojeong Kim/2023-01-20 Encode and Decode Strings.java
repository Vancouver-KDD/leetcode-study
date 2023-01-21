import java.util.*;

class Solution {
    /*
     * @param strs: a list of strings
     * @return: encodes a list of strings to a single string.
     */
    public String encode(List<String> strs) {
        // write your code here
        if(strs.size() == 0 || strs == null) {
            return "";
        }
        StringBuffer sb = new StringBuffer();

        for(String str : strs) {
            if(str == null || str.length() == 0 ) {
                sb.append("0# ");
            }else {
                sb.append(str.length() + "#" + str);
            }
            sb.append("/");
        }
        return sb.toString();
    }

    /*
     * @param str: A string
     * @return: dcodes a single string to a list of strings
     */
    public List<String> decode(String str) {
        // write your
        List<String> result = new ArrayList<>();

        if(str.length() == 0 || str == null) return result;

        String [] arr = str.split("/");
    
        for(int i = 1; i<arr.length;i++) {
            String [] each = arr[i].split("#");
            result.add(each[1]);
        }
        return result;

    }
}