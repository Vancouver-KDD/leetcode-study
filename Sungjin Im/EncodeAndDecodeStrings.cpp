// Encode And Decode Strings
// :author: SJ
// :date: Jan 27 2023
//
// Design an algorithm to encode
//      a list of strings
//          to a string.
//
// The encoded string is then sent over the network 
//      and is decoded back to the original list of strings.
//
// Please implement encode and decode
//
// Example 1
// Input: ["lint","code","love","you"]
// Output: ["lint", "code", "love", "you"]
//
// Example 2
// Input: ["we", "say", ":", "yes"]
// Output: ["we", "say", ":", "yes"]
//

#include <iostream>
#include <string>
#include <vector>

using namespace std;

string encode(vector<string>& strs) {
    string s;
    for (size_t i = 0; i < strs.size(); ++i) {
        size_t len = strs[i].length();
        string tmp;
        for (size_t i = 0, mask = 0xff; i < sizeof(size_t); ++i, mask <<= 8) {
            tmp.push_back(len & mask);
        }
        reverse(tmp.begin(), tmp.end());
        s.append(tmp);
        s.append(strs[i]);
    }

    return s;
}

vector<string> decode(string s) {
    vector<string> strs;
    size_t pos = 0;

    while (pos + sizeof(size_t) <= s.length()) {
        size_t len = 0;
        for (size_t i = 0; i < sizeof(size_t); ++i) {
            len <<= 8;
            len += static_cast<unsigned char>(s[pos++]);
        }

        strs.push_back(s.substr(pos, len));
        pos += len;
    }

    return strs;
}

int main()
{
    //vector<string> strs = { "lint", "code", "love", "you" };
    vector<string> strs = { "we", "say", ":", "yes" };

    string s = encode(strs);

    vector<string> ans = decode(s);

    for (vector<string>::iterator it = ans.begin(); it != ans.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;

    return 0;
}