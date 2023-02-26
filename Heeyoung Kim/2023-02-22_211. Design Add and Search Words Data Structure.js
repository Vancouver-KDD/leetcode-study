var WordDictionary = ()=>{
    this.trie = {};
}

WordDictionary.prototype.addWord = (word) => {
    let root = this.trie;
    for(let i=0; i<word.length; i++) {
        if(root[word[i]] === null) root[word[i]] = {};
        root = root[word[i]];
    }
    root.isEnd = true;
}

WordDictionary.prototype.search = (word) => {
    return this.dfs(word, 0, this.trie);
}

WordDictionary.prototype.dfs = (word, index, node)=> {
    if(index === word.length) return node.isEnd == true;
    if(word[index] == '.') {
        for(let key in node) {
            if(this.dfs(word, index+1, node[key])) return true;
        }
    }else {
        if(node[word[index]] != null){
            return this.dfs(word, index+1, node[word[index]]);
        }
    }

    return false;
}