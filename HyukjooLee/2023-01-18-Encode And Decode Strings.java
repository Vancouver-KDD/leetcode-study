/**
 * Design an algorithm to encode a list of strings to a string.
 * The encoded string is then sent over the network and is decoded back to the original list of strings.
 * Please implement encode and decode in java
 */

public class Codec {
    final char SEPARATOR = ";";

    // e.g. 
    // ["Hello" , "World"]
    // => "5;Hello5;World"
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String str : strs) {
            sb.append(str.length());
            sb.append(SEPARATOR);
            sb.append(str);
        }
        return sb.toString();
    }

    public List<String> decode(String s) {
        return Arrays.asList(s.split(SEPARATOR));
    }
}



public class Codec {
    /*
     * @param strs: a list of strings
     * @return: encodes a list of strings to a single string.
     */
    
    final char SEPARATOR = ";";

    public String encode(List<String> strs) {
        return String.join(separator, strs);
    }

    /*
     * @param str: A string
     * @return: dcodes a single string to a list of strings
     */
    public List<String> decode(String str) {
        return Arrays.asList(str.split(separator));
    }
}

