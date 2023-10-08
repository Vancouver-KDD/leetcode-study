class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        int i = 0;
        int j = 0;
        List<int[]> result = new ArrayList<>(); // List of int arrays for the result

        while (i<firstList.length && j<secondList.length){
            int a[] = firstList[i]; // first interval
            int b[] = secondList[j];
            
            if(b[0]<=a[1] && b[0]>=a[0]) // b is inside a
                result.add(new int[]{b[0], Math.min(a[1], b[1])});
            else if(a[0]<=b[1] && a[0]>=b[0]) // a is inside b
                result.add(new int[]{a[0], Math.min(a[1], b[1])});
            
            if(a[1]<=b[1])
                i++;
            else
                j++;
        }
        int ans[][] = new int[result.size()][2];
        
        for(i=0;i<result.size();i++){
            ans[i] = result.get(i);
        }
        return ans;
        
    }
}