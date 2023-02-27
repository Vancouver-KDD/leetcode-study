
public class LC_2023_02_26_ImplementTriePrefixTree {
	//클래스 생성해야함
	class TrieNode{
	    public boolean isWord;
	    public TrieNode[] children = new TrieNode[26]; // 알파벳 갯수 =26
	    public TrieNode(){}
	}


	class Trie {
	    private TrieNode root;


	    public Trie() {
	        root = new TrieNode();
	    }
	    
	    public void insert(String word) {
	        TrieNode ws = root;
	        for(int i = 0 ; i < word.length();i++){
	            char c = word.charAt(i);
	            if(ws.children[c -'a'] == null){ // children에 캐릭터 c가 없으면 
	                ws.children[c-'a'] = new TrieNode(); // 노드 만들어내기
	            }
	            ws = ws.children[c - 'a']; // 있으면 안에 넣기
	        }
	        ws.isWord = true;
	    }
	    
	    public boolean search(String word) {
	        TrieNode ws = root;
	        for(int i = 0 ; i < word.length();i++){
	            char c = word.charAt(i);
	            if(ws.children[c-'a'] == null) return false;
	            ws = ws.children[c -'a'];
	        }
	        return ws.isWord; // 좀 헷갈림 
	    }
	    
	    public boolean startsWith(String prefix) {
	        TrieNode ws = root;
	        for(int i = 0 ; i < prefix.length();i++){
	            char c = prefix.charAt(i);
	            if(ws.children[c - 'a'] == null) return false;
	            ws= ws.children[c-'a'];
	        }
	        return true;
	    }
	}


}
