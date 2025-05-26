class PrefixTree {
public:
    PrefixTree() {

    }

    void insert(string word) {
        s.insert(word);
    }

    bool search(string word) {
        if(s.find(word) != s.end()) return true;
        return false;
    }

    bool startsWith(string prefix) {
        for (auto it = s.begin(); it != s.end(); it++) {
            if (it->substr(0, prefix.size()) == prefix) {
                return true;
            }
        }
        return false;
    }
private:
    set<string> s;
};
