public class Solution {
    public IList<string> TopKFrequent(string[] words, int k) {
        Dictionary<string,int> dic = new();
        IList<string> result = new List<string>();
        foreach(var word in words){
            if(dic.ContainsKey(word)){
                dic[word]++;
            }else{
                dic.Add(word,1);
            }
        }
        return dic.OrderByDescending(kv => kv.Value).
                    ThenBy(kv=>kv.Key).
                    Take(k).
                    Select(kv=>kv.Key).
                    ToList();
    }
}
