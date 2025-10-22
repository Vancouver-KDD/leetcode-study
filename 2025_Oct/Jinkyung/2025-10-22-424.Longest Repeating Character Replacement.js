/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    let maxFreq=0;
    let start=0, end=0;
    let freq = new Array(26).fill(0); //[0,0,0,0,0,0,0,0...]
    //문자열의 빈도수를 구한다.
    for(end=0;end<s.length;end++){
        // const index = s.charCodeAt(end)-65;
        const index = s[end].charCodeAt(0)-65
        freq[index]++;
        //가장 빈도수가 많은 문자열을 구해주고
        maxFreq = Math.max(maxFreq,freq[index]);
        //window의 크기에서 문자열의 빈도수가 가장 큰것을 뺐을때, k(바꿀수 있는 문자의 수)보다 크면 윈도우를 줄여야함
        // 만약에 윈도우의 크기가 6인데, A가 3이라고 했을때, 바꿔야하는 수는 3인데, K가 2이므로 변경 불가 -> 윈도우 줄임
        if(end-start+1 - maxFreq>k){
            freq[s[start].charCodeAt(0)-65]--;
            start++;
        }
    }
    //전체 윈도우의 크기를 반환해주면 된다.
    return end-start+1;
};


/**
    s = ABAB k =2
    chars = 'A' B->A AAAA maxLen = 4
    'B'->A BBBB maxLen = 4
    output 4

    ex2)
    s = AABABBA k=1
    A->B 1.AAAABBA -> MaxLen = 4
     2. AABAABA -> MaxLen = 2
     3. AABABAA -> MaxLen=2

     two pointer and set
 */