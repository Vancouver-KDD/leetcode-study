/**
 * A phrase is a palindrome if, after converting all uppercase letters 
 * into lowercase letters and removing all non-alphanumeric characters, 
 * it reads the same forward and backward. Alphanumeric characters include letters and numbers.
 */
    
// 1. using stack with string builder
// time complexity is O(n) as we traverse elements of char array & stack each other
public static boolean isPalindrome(String s) {
	// Covert all chars in a given string into lower cases
	String t = s.toLowerCase();
	String reveredStr = "";
	// Define a string builder to make a comparable string (should be all lower
	// cases & numeric chars)
	StringBuilder sb = new StringBuilder();
	// Initialize Stack<Character>, we will use push & pop functions
	Stack<Character> stack = new Stack<>();
	for (int i = 0; i < t.length(); i++) {
		// Remove all non-alphanumeric characters, and append each chars to the String
		// builder
		if (Character.isLetterOrDigit(t.charAt(i))) {
			stack.push(t.charAt(i));
			sb.append(t.charAt(i));
		}
	}
	while (!stack.isEmpty())
		reveredStr += stack.pop();
	return reveredStr.equals(sb.toString());
}

// 2. using only String builder 
// time complexity is O(n)
public static boolean isPalindrome_2(String s) {
	// Initialize reversed string and String builder
	String reversedStr = "";
	StringBuilder sb = new StringBuilder();
	// Convert the string into a char array because we are gonna check if the each
	// chars is letter or digit also covert all into lower cases
	char[] chArr = s.toCharArray();
	for (int i = 0; i < chArr.length; i++) {
		if (Character.isLetterOrDigit(chArr[i])) {
			sb.append(Character.toLowerCase(chArr[i]));
		}
	}
	// New array which is filtered.
	String newStr = sb.toString();
	// Reverse the string builder
	reversedStr = sb.reverse().toString();
	return newStr.toString().equals(reversedStr);
}

 // 3. two pointer Approach
// time complexity is O(N), not O(logN) 
// iterate over the entire string once to compare each pair of characters pointed by two pointers
public static boolean isPalindrome_3(String s) {
	int left = 0;
	int right = s.length() - 1;
	while (left <= right) {
		char leftChar = s.charAt(left);
		char rightChar = s.charAt(right);
		if (!Character.isLetterOrDigit(leftChar)) {
			left++;
			continue;
		} 
		if (!Character.isLetterOrDigit(rightChar)) {
			right--;
			continue;
		}
		if (Character.toLowerCase(leftChar) != Character.toLowerCase(rightChar)) {
			return false;				
		}
		
		left++;
		right--;
	}
	return true;
}


// review

// preprocess string
// 3 * O(N), where n is the length of the input string => O(N)
// 3 * O(N), sb, stack, reveredStr 
private static String preprocessString(String s) {
    
    // to lowercase
    s = s.toLowerCase();
    StringBuilder sb = new StringBuilder();

    // remove non-numeric values
    for(char c: s.toCharArray()) {
        // check chars are letters of digits
        if(Character.isLetterOrDigit(c)) {
            sb.append(c);
        }
    }
    return sb.toString();
}

isPalindrome(String s) {

    s = preprocessString(s);
    Stack<Character> stack = new Stack<>();
    for(char c : s.toCharArray()) {
        stack.push(c);
    }

    String reversedString = "";
    while(!stack.empty()) {
        reversedString += stack.pop();
    }
    return s.equals(reversedString);
}


// if a input string is very long, this solution can be inefficient
// because it requires too much memory space to store filtered string ,reversed string, also this solution uses stack
// to handle with the problems, we can use two pointer approach to solve this problem

private static String preprocessString(String s) {
    
    // to lowercase
    s = s.toLowerCase();
    StringBuilder sb = new StringBuilder();

    // remove non-numeric values
    for(char c: s.toCharArray()) {
        // check chars are letters of digits
        if(Character.isLetterOrDigit(c)) {
            sb.append(c);
        }
    }
    return sb.toString();
}


// s.preprocessString(s); // it takes N space complexity though
int l = 0;
int r = s.length() - 1;

while(l <= r) {
	char lChar = s.chatAt(l);
	char rChar = s.charAt(r);

	if (!Character.isLetterOrDigit(leftChar)) {
			left++;
			continue; // break the iteration
	} 
	
	if (!Character.isLetterOrDigit(rightChar)) {
			right--;
			continue;
	}

	if(Character.toLowerCase(lChar) != Character.toLowerCase(rChar)) return false;

	left++;
	right--;
}

return true;