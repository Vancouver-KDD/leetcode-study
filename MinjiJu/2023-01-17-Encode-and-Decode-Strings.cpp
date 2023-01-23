class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        for (string &s : strs) encoded += to_string(s.size()) + '.' + s;
	    return encoded;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        for (int i = 0, n = 0; i < s.size(); i += n, n = 0) {
		    while (isdigit(s[i])) n = 10 * n + (s[i++] - '0');
		    decoded.push_back(s.substr(++i, n));
	    }
	    return decoded;
    }
private:
    string encoded = "";
    vector<string> decoded = {};
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));