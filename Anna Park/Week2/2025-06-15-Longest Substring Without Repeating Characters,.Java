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

    // Create a HashSet to store unique characters in current window
    Set<Character> set = new HashSet<>();
    int left = 0, max = 0; // Initialize left pointer and maximum length

    // Iterate through the string with right pointer
    for (int right = 0; right < s.length(); right++) {
        char c = s.charAt(right); // Get the current character

        // If duplicate character is found, shrink the window from the left
        while (set.contains(c)) {
            set.remove(s.charAt(left)); // Remove the leftmost character
            left++; // Move the left pointer to the right
        }

        set.add(c); // Add the current character to the set

        // Update maximum length if current window is larger
        max = Math.max(max, right - left + 1);
    }

    return max; // Return the length of the longest substring without repeating characters
}
