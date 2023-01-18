
//2023-01-17
// strs[i].length 의 max 가 200 이니까 앞자리 character 3개를 length 로 fix 
// ex) input: ["Hello","World"] -> 005 + Hello + 005 + World = "005Hello005World"
//     input: [""] -> 000 + ""  -> "000"
//Time Complexity: O(N)
//Space Complexity: O(1) <-- encode, O(N) <-- decode (리턴위한 배열을 할당. 이걸빼면 똑같이 O(1) 이긴 함. )
public class Codec{
    public String encode(List<String> strs){
        if(strs == null || strs.size() == 0){
            return "";
        }

        StringBuilder encodedStr = new StringBuilder();

        for(String str: strs){
            int length = str.length();
            char[] lengthCh = new char[3];
            lengthCh[0] = (char)(length /100 + '0');
            length = length %100;
            lengthCh[1] = (char)(length /10 + '0');
            lengthCh[2] = (char)(length %10 + '0');

            encodedStr.append(lengthCh);
            encodedStr.append(str);
            
        }

        return encodedStr.toString();
    }

    public List<String> decode(String s){
        List<String> decodedList = new ArrayList<String>();
        if(s == null || s.length() == 0){
            return decodedList;
        }

        int count = 0; 
        while(count < s.length()){
            String head = s.substring(count, count+3);
            int length = Integer.parseInt(head);
            decodedList.add(s.substring(count+3, count+3+length));
            count = count+3+length;
        }

        return decodedList;
    }
}

//아래와 같은 규칙을 가지고 incoding 할 것임. 
//'length of string' + '#' + 'string' 
//Time complexity : O(N) -> both for encode and decode, where N is a number of strings in the input array.
// Space complexity : O(1) for encode to keep the output, since the output is one string. O(N) for decode keep the output, since the output is an array of strings
/*
public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder encodedStr = new StringBuilder();
        for(String str : strs){
            encodedStr.append(str.length());
            encodedStr.append('#');
            encodedStr.append(str);
        }
        //["Hello","World"] -> "5#Hello5#World""

        return encodedStr.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> decodedList = new ArrayList<>();

        int position = 0;
        int length = 0;
        int index = 0; 
        while(index < s.length()){
            char ch = s.charAt(index);
            if(ch == '#'){
                String numStr = s.substring(position, index);
                length = Integer.parseInt(numStr);
                
                String str = s.substring(index+1, index+1+ length);
                decodedList.add(str);
                position = index+1+length;
                index = position;
            }else{
                index++;
            }
        }
        //ex1) "5#Hello5#World"->length(0,1):5,index:1, str(2,7):hello, new index:7
        //      ->  length(7,8):5, index:8, str(9,14):Wordl
        //ex2) "0#0#" -> length(0,1):0, index:1, str(2,2), new index:2
        //      -> length(2,3):0 , index: 3, str(4,4)
        return decodedList;
    }
}
*/
// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));

