class WordDictionary {
public:
    WordDictionary() {

    }

    void addWord(string word) {
        s.push_back(word);
    }

    bool search(string word) {
        for (string& str : s) {
            if (str.size() != word.size()) continue;

            int i = 0;
            while (i < str.size()) {
                if (str[i] == word[i] || word[i] == '.') {
                    i++;
                } else {
                    break;
                }
            }

            if (i == str.size()) {
                return true;
            }
        }

        return false;
    }


private:
    vector<string> s;
};
