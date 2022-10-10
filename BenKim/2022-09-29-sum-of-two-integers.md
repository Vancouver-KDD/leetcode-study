# 371. Sum of Two Integers

> problem link: https://leetcode.com/problems/sum-of-two-integers/  
> submission detail: https://leetcode.com/submissions/detail/814854583/

- bit operation을 사용한다
- python의 int는 4바이트가 아닌 arbitrary precision이기 때문에 Java를 사용해 풀이한다
- XOR은 다른경우에 1를 반환
- AND는 둘다 1인경우에 1을반환

```java
class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            
            // tmp는 캐리되는 자리수만 남게된다
            int tmp = (a & b) << 1;

            // XOR 연산을 통해 1과 0인경우 1로 계산한다
            a = a ^ b;
            b = tmp;
        }
        return a;
    }
}        
```