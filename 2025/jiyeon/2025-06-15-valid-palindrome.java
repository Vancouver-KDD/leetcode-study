class IsPalindrome {
    public boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            char left = s.charAt(i);
            char right = s.charAt(j);
            if (!Character.isLetterOrDigit(left)) {
                i++;
                continue;
            } else if (!Character.isLetterOrDigit(right)) {
                j--;
                continue;
            } else if (Character.toLowerCase(left) != Character.toLowerCase(right)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}