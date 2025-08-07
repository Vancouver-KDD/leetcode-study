```
import java.util.Arrays;

public class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g); // 아이의 욕심
        Arrays.sort(s); // 쿠키 크기

        int child = 0, cookie = 0;

        while (child < g.length && cookie < s.length) {
            if (s[cookie] >= g[child]) {
                child++;  // 이 아이 만족시킴
            }
            cookie++;
        }

        return child;
    }
}

```
