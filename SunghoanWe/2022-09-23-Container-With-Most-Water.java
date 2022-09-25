import java.sql.Array;
import java.util.Arrays;

public class ContainerWithMostWater {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

//    public int maxArea(int[] height) {
//    	int vertical = 0;
//    	int horizontal = 0;
//    	int area = 0;
//    	int maxArea = 0;
//    	for(int i=0; i < height.length; i++) {
//    		for(int j=0; j < height.length; j++) {
//    			if (i != j) {
//    				 vertical = Math.min(height[i], height[j]);
//    				 horizontal = Math.abs(Math.abs(i)-Math.abs(j));
//    				 area = vertical * horizontal;
//    				 if (maxArea < area) {
//    					 maxArea = area;
//    				 }
//    			}
//    		}
//    		
//    		
//    	}
//    	return maxArea;
//    }

    public int maxArea(int[] height) {
        int maxarea = 0;
        int leftIndex = 0; 
        int rightIndex = height.length - 1;
        while (leftIndex < rightIndex) {
            int width = rightIndex - leftIndex;
            maxarea = Math.max(maxarea, Math.min(height[leftIndex], height[rightIndex]) * width);
            if (height[leftIndex] < height[rightIndex]) {
                leftIndex++;
            } else {
                rightIndex--;
            }
        }
        return maxarea;
    }	
	
}
