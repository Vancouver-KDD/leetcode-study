//Similar questions
//  452. Minimum Number of Arrows to Burst Balloons  (premium)
//  이문제에서는 [1,2][2,3] -> 이게 overlapping 관계가 아닌가보다. 
// 어떤식으로 overlapping 되지? 
//  [[1,2],[1,3]] <-- 이런식으로 완전히 포함관계의 overlapping 인지 
//  [[1,5],[3,6]] <-- 이런식으로 걸치는 overlapping 도 있는건지 -> 이경우도 존재. 
//                  합치는건 아니고 overlapping 되는게 있으면 remove 만 함. 그럼 앞에것과 뒤엣것중 아무거나???
//  input: [[1,3],[4,7],[1,7]] -> output: 1
//  input: [[1,5],[3,8],[5,8]] -> output: 1
//  input: [[0,2],[1,3],[2,4],[3,5],[4,6]] -> output: 2

// 1) end 를 기준으로 sorting
//    : 이렇게 하는 이유는 겹치는것 제거할때, end 가 더 큰 것을 제거해야 
//      그뒤에 나올 세트들이 겹칠 확률이 줄어듬. 
//      ex) [3,5] [2,7] [5,8] <-- 이런경우, 0번 1번중, end 가 더큰 2번을 제거해야 2번과 겹치지 않게됨. 
//      ex) [3,5] [4,7] [5,8] <-- 이경우도 역시, 0, 1번중 end가 더 큰 1번을 삭제해야 유리. 
// 2) 0부터 n-1 까지 비교시작. 
//     2-1) (i-1)의 end <= (i)의 start 이면 겹치지 않으면 count 증가,
//          그리고 end = (i)의 end 로 업데이트
// 3) (원래 배열 길이 - count)구하면 => 제거한 개수      
//

//2023-10-04 

class Solution{
    public int eraseOverlapIntervals(int[][] intervals){
        if(intervals == null || intervals.length <= 0 || intervals[0].length <= 0){
            return 0;
        }
        
        Arrays.sort(intervals, (a,b)->(a[1]-b[1]) ); //sort by 'end' element
        
        int remove = 0;
        int prevEnd = Integer.MIN_VALUE;
        for(int i = 0; i < intervals.length; i++){
            if(prevEnd > intervals[i][0]){
                remove++;
            }else{
                prevEnd = intervals[i][1];
            }
        }
        return remove;
    }
}

