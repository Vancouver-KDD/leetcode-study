// Valid_Anagrams.cpp : This file contains the 'main' function. Program execution begins and ends there.
// 
// Given two strings s and t, 
// return true if t is an anagram of s, and false otherwise.
//
// Example 1:
// Input: s = "anagram", t = "nagaram"
// Output : true
//
// Example 2 :
// Input : s = "rat", t = "car"
// Output : false
//


#include <iostream>
#include <string>

using namespace std;

bool isAnagram(string s, string t)
{
    if (s.length() != t.length())
    {
        return false;
    }

    string temp("");
    for (string::iterator it = s.begin(); it != s.end(); ++it)
    {
        for (string::iterator it2 = t.begin(); it2 != t.end(); ++it2)
        {
            if (*it == *it2)
            {
                temp += *it2;
                t.erase(it2);

                cout << "s: " << s << endl;
                cout << "t: " << t << endl;
                cout << "temp: " << temp << endl;
                cout << "\n\n";

                break;
            }
        }
    }

    if (s.compare(temp) == 0 && t.empty() == true)
    {
        return true;
    }

    return false;
}

int main()
{
    int ex_num = 1;
    string s = "";
    string t = "";
    bool result = false;

    switch (ex_num)
    {
        case 1:
            s = "anagram";
            t = "nagaram";
            break;

        case 2:
            s = "rat";
            t = "cat";
            break;

        default:
            break;
    }

    result = isAnagram(s, t);

    if (result == true) {   cout << "true" << endl;     }
    else                {   cout << "false" << endl;    }

    return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

