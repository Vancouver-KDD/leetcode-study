//Using map and set, not trie
import java.util.*;

class WordDictionary {
    Map<Integer, List<String>> map = new HashMap<>();
    //can put it in the list, find O(N) 
    //map, find quicker

    public WordDictionary() {
        
    }
    
    public void addWord(String word) {
        int index = word.length();
        if(!map.containsKey(index)) {
            List<String> list = new ArrayList<>();
            list.add(word);
            map.put(index, list);
        }else {
            map.get(index).add(word);
        }
    }
    
    public boolean search(String word) {
        int index = word.length();
        if(!map.containsKey(index)) {
            return false;
        }
        List<String> list = map.get(index);
        if(isWords(word)){
            return list.contains(word);
        }

        for(String s : list ) {
            if(isSame(s, word)) {
                return true;
            }
        }
        return false;
    }
    boolean isWords(String s){
        for(int i = 0; i < s.length(); i++){
            if(!Character.isLetter(s.charAt(i))){
                return false;
            }
        }
        return true;
    }

    boolean isSame(String a, String search) {
        if(a.length() != search.length()) {
            return false;
        }
        for(int i = 0;i<a.length();i++) {
            if(search.charAt(i) != '.' && search.charAt(i) != a.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */

 //But I think mapping every character instead string is a more memory-saving approach.
//Trie 방식
class WordDictionary2 {
    private static final int R = 26;
   private Node root;
   private static class Node {
       boolean isEnd = false; // 각 노드에 제일 끝 노트인지 아닌지 알려주는 플래그를 다는 것
       Node[] next = new Node[R];
   }


   public WordDictionary2() {
       root = new Node();
   }
   
   public void addWord(String word) {
       root = insert(word, root, 0);
   }

   private Node insert(String word, Node x, int d) {
       if(x==null) x= new Node();
       if(d == word.length()) {
           x.isEnd = true;
           return x;
       }
       char c = word.charAt(d);
       x.next[c-'a'] = insert(word, x.next[c-'a'], d+1);
       return x;
   }
   
   public boolean search(String word) {
      return search(word, root, 0);
   }

   private boolean search(String pat, Node x, int d) {
       if(x== null) return false;
       if(d==pat.length()) return x.isEnd;
       char next = pat.charAt(d);
       boolean answer = false;
       for(char c = 0; c<R;c++) {
           if( next == '.' || c==next-'a') { 
               //otherwise. word may contain dots '.' where dots can be matched with any letter.
               answer = answer || search(pat, x.next[c], d+1);
           }
       }
       return answer;
   }

}

/**
* Your WordDictionary object will be instantiated and called as such:
* WordDictionary obj = new WordDictionary();
* obj.addWord(word);
* boolean param_2 = obj.search(word);
*/