function threeSum(nums: number[]): number[][] {
    const result = [];
    nums.sort((a,b)=>a-b)
    // i, L ,H
    for(let i=0;i<nums.length-2;i++){
        if(i>0 && nums[i]===nums[i-1])continue;
        let low = i+1;
        let high = nums.length-1
       
        while(low<high){
             let sum = nums[i]+nums[low]+nums[high];
             if(sum<0)low++;
             else if(sum>0) high--;
             else{
                 
            
                result.push([nums[i],nums[low],nums[high]]);
               
                //중복 제거
                while(low<high && nums[low]===nums[low+1])low++;
                while(low<high && nums[high]===nums[high-1])high--;
                 low++;
                high--;
             }
            
        }
    }

    return result;
};
// i  L        
//[-4,-1,-1,0,1,2]
//              H

/**
1. 아이디어
 - sorting해서 오름차순으로 정렬
 - 3개의 포인터를 사용해서 i,L(low),H(high) 합을 구함
 - sum이 0보다 작다면, L의 값이 더 커져야하므로 Low++
 - 0보다 크다면, H의 값이 더 작아져야하므로 High--
 - 0과 같다면 결과값에 넣어주기
 - 중복 제거

 */