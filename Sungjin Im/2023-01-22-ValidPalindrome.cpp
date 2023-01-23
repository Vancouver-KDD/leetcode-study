// Valid Palindrome
// :author: SJ
// :date: Jan 22 2023
//
// A phrase is a palindrome if,
// after converting all uppercase letters into lowercase letters
// and removing all non-alphanumeric characters,
// it reads the same forward and backward.
// Alphanumeric characters include letters and numbers.
//
// Example 1:
// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation : "amanaplanacanalpanama" is a palindrome.
//
// Example 2:
// Input: s = "race a car"
// Output: false
//
// Example 3 :
// Input: s = " "
// Output: true
//

#include <iostream>
#include <string>
#include <locale>         // std::locale, std::isupper, std::tolower

using namespace std;

#define _RUN_MODE


int main()
{
	string s = { "A man, a plan, a canal: Panama" };
//	string s = { "race a car" };
//	string s = { "" };
	
	string converted_s = "";
	string reversed_s = "";

	locale loc;

	// after converting all uppercase letters into lowercase letters
	for (string::iterator it = s.begin(); it != s.end(); ++it) {
		if (isupper(*it, loc)) {
			*it = tolower(*it, loc);
		}
	}

	// and removing all non-alphanumeric characters,
	for (string::iterator it = s.begin(); it != s.end(); ++it) {
		// ASCII numbers: 48~57
		// ASCII lowercase: 97-122
		if (int(*it) >= 48 && int(*it) <= 57 ||
			int(*it) >= 97 && int(*it) <= 122 ) {
			converted_s.push_back(*it);
		}
	}

	// make the string reverse
	for (string::reverse_iterator rit = converted_s.rbegin(); rit != converted_s.rend(); ++rit) {
		reversed_s.push_back(*rit);
	}

#ifndef _RUN_MODE		// means if debug mode
	cout << "s: " << s << endl;
	cout << "converted_s: " << converted_s << endl;
	cout << "reversed_s: " << reversed_s << endl;
#endif

	// compare the forward and backward
	if (converted_s.compare(reversed_s) == 0) {
		cout << "true";
	}
	else {
		cout << "false";
	}
											
	cout << "\n\n";

	return 0;
}