/**
 * @param {string} s
 * @return {number}
 */

 /**
 1. 아이디어
    - sliding window 알고리즘 사용
    - set과 투 포인터를 통해 첫번째 값부터 넣고, set에 있는지 확인
    - set의 길이를 max에 계속 업데이트
 2. 변수 설정
    - set(chars), two pointer(start, end), max Length(maxLen)
 3. 시간복잡도, 공간복잡도
    - sliding window이므로 O(n)
  */

var lengthOfLongestSubstring = function(s) {
    let maxLen = 0
    let chars = new Set()
    let start=0,end=0;

    while(end<s.length){
        //만약에 s의 s[end]가 set에 없다면? -> add Set, end++
        //set에 있다면? -> delete set, start++ , max 업데이트

        if(!chars.has(s[end])){
            chars.add(s[end]);
            end++;
        }else{
            chars.delete(s[start]);
            start++;            
        }
        maxLen = Math.max(maxLen,chars.size)        
    }
    return maxLen;
};