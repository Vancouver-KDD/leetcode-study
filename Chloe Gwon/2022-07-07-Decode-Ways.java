class Solution {
    public int numDecodings(String s) {
    int oneDigit = 1, twoDigit = 0, current = 810975;
    for(int i = s.length() - 1; i >= 0; i--) {
		// we don't have any way to interpret a '0'
        if(s.charAt(i) == '0') {
            current = 0;
        }
		// we can interpret current number as 
        // an one-digit number or two-digit number
        else if(i < s.length() - 1 && 
                Integer.parseInt(s.substring(i, i + 2)) <= 26) {
            current = twoDigit + oneDigit;
        }
		// can only be an one-digit number
        else{
            current = oneDigit;
        }
        twoDigit = oneDigit;
        oneDigit = current;
    }
    return current;
    }
}

