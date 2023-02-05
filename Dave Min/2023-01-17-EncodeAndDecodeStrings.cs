public class Codec {

    public const string slash = "/";
    // Encodes a list of strings to a single string.
    public string encode(IList<string> strs) {
        StringBuilder strBder = new StringBuilder();
        foreach(var str in strs){
            strBder.Append(str.Length);
            strBder.Append(slash);
            strBder.Append(str);
        }

        return strBder.ToString();
    }

    // Decodes a single string to a list of strings.
    public IList<string> decode(string s) {
        IList<string> result = new List<string>();
        int from = 0;
        int slashIdx =0;
        int len =0;
        while(from < s.Length){
            slashIdx = s.IndexOf("/", from);
            len = int.Parse(s.Substring(from, slashIdx-from));
            string tmp = s.Substring(slashIdx +1, len);
            result.Add(s.Substring(slashIdx +1, len));
            from = slashIdx + len+1;
        }
        return result;
    }
}