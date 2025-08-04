## 374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

```
/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int left = 1;
        int right = n;
        int pick = n/2;
        int returnValue = guess(pick);
    
        while(returnValue != 0){
            pick = left + (right- left) / 2 ;
            returnValue = guess(pick);
            if(returnValue == -1 ){ //higher
                right = pick-1;
             }else if( returnValue == 1 ){ //lower
                left = pick+1;    
             }            
        }

        return pick;

        
    }
}
```

### Time Complexity : O(log n)
Because the solution uses binary search, the search range is cut in half with each iteration.
At most, it takes log₂(n) steps to find the correct number, so the runtime is logarithmic with respect to n.


### Space Complexity : O(1)
The algorithm only uses a constant amount of memory — a few integer variables like left, right, pick, and returnValue.
No additional data structures or recursion are used, so the space complexity remains constant.
