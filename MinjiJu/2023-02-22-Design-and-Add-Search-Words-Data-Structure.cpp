struct TrieNode{
    bool isKey;
    TrieNode* next[26];
    TrieNode():isKey(false){
        memset(next, NULL, sizeof(next));
    }
};

class WordDictionary {
public:
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* node = root;
        for(auto c: word){
            if(!node->next[c - 'a']) node->next[c - 'a'] = new TrieNode();
            node = node->next[c - 'a'];
        }
        node->isKey = true;
    }
    
    bool search(string word) {
        return helper(word, root);
    }

private:
    TrieNode* root;
    
    bool helper(string word, TrieNode* node){
        for(int i = 0; i < word.size(); i++){
            char c = word[i];
            if(c != '.'){
                if(!node->next[c - 'a']) return false;
                node = node->next[c - 'a'];
            }
            else{
                bool found = false;
                int j = 0;
                for(; j < 26; j++){
                    if(node->next[j]) found |= helper(word.substr(i + 1), node->next[j]);
                    if(found) return true;
                }
                if(j == 26) return false;
            }
        }
        return node->isKey;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */