class Solution {
public:
    int numDecodings(string s) {
        
        // s[i] maps to dp[i+1]
        vector<int> dp(s.length()+1,1);
        
        if(s.empty() || s[0]=='0') return 0;
        
        for(int i=1; i<s.length(); i++){
            int val = (s[i-1]-'0')*10+(s[i]-'0');
            
            if(s[i]=='0'){
                if(s[i-1]!='1' && s[i-1]!='2') return 0;
                else dp[i+1] = dp[i-1];
            }
            else if(10<val && val<27){
                dp[i+1] = dp[i-1] + dp[i];
            }
            else{
                dp[i+1] = dp[i];
            }
        }
        return dp[s.length()];
    }
};

/*
class Solution {
public:
    int numDecodings(string s) {
        vector<int> dp(s.length()+1,1);     // s[i] maps to dp[i+1];
        if(!s.length() || s[0]=='0') return 0;
        
        for(int i=1;i<s.length();i++){
            int num=(s[i-1]-'0')*10+(s[i]-'0');
            if(s[i]=='0'){
                if(s[i-1]!='1' && s[i-1]!='2') return 0;
                else dp[i+1]=dp[i-1];
            }
            else if(10<num && num<27) dp[i+1]=dp[i-1]+dp[i];
                else dp[i+1]=dp[i];
        }
        return dp[s.length()];
    }
};

/*
    int numDecodings(string s) {
        int p = 1, pp, n = s.size();
        for(int i=n-1;i>=0;i--) {
            int cur = s[i]=='0' ? 0 : p;
            if(i<n-1 && (s[i]=='1'||s[i]=='2'&&s[i+1]<'7')) cur+=pp;
            pp = p;
            p = cur;
        }
        return s.empty()? 0 : p;   
    }
    
*/