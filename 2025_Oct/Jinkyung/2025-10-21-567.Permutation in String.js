class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    /**
     * 1. 아이디어
     *  - s1의 문자 갯수 세서 array에 저장 = count1
     *  - s2의 문자갯수를 세서 array에 저장 = count2
     *  - window를 보면서  window의 크기가 커지면, start의 수를 줄이고, start++
     *  - count1, count2의 배열이 같은지 확인 return true
     */

    
    checkInclusion(s1, s2) {
        let count1=Array(26).fill(0);
        let count2=Array(26).fill(0)
        let start=0,end=0;

        //s1의 문자열 빈도수 구하기
        for(let c of s1){
            count1[c.charCodeAt(0)-97]++; //a:1,b"1
        }

        for(end=0;end<s2.length;end++){
            //end를 옮겨가면서 s2[end]의 문자열 빈도수 구하기 
            count2[s2[end].charCodeAt(0)-97]++

            //window의 크기가 커지면, start를 제거하고, 옮기기
            if(end-start+1>s1.length){
                count2[s2[start].charCodeAt(0)-97]--;
                start++;
            }
             //count1과 count2를 비교
            //전체 유니코드의 갯수를 비교하면서, 두개의 count array가 다르다면 false 반환
            if(this.arrayEqual(count1,count2)) return true;
        }
        return false
    }
    arrayEqual(count1,count2){
         for(let i=0;i<26;i++){ 
                if(count1[i]!==count2[i])return false
               
             }
             return true
    }

}
