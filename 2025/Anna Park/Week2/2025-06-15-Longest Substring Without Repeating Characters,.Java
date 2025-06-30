class Longest Substring Without Repeating Characters {
    public int lengthOfLongestSubstring1(String s) {

        String temp = "";
        List<String> sub = new ArrayList<>();

        //do for loop putting character of s
        for (char c: s.toCharArray()){
        //if same character happen, then put in list
            if (temp.indexOf(c) != -1){ //if duplicate
                sub.add(temp);
                temp = "" + c;
            } else{
                temp += c;
            }
        }
        sub.add(temp);

        //return max length of list
        int max = 0;
        for (int i=0; i<sub.size(); i++){
            if (sub.get(i).length() >= max){
                max = sub.get(i).length();
            }
        }

        return max;
    }

    public int lengthOfLongestSubstring2(String s) {

        //make Set to store substring
        Set<Character> set = new HashSet<>();
        int left = 0, max = 0; //initiate window, max

        //for loop to make substring
        for(int right = 0; right<s.length(); right++){
            char c = s.charAt(right); //extend window

            //if duplicate? then move window
            while(set.contains(c)){
                set.remove(s.charAt(left));
                left++;
            }

            set.add(c); //put c in hashset
            max = Math.max(max, right - left + 1);
        }

        return max;
        }
    }
}
