public class NumbeOf1Bits {
	
//    public int hammingWeight(int n) {
//    	System.out.println(Integer.toBinaryString(-3));
//    	String temp = Integer.toBinaryString(n);
//        System.out.println(temp);
//    	int count = 0;
//    	for (int i=0; i < temp.length(); i++) {
//    		if (temp.charAt(i) == '1') {
//    			count++;
//    		}
//
//    	}
//        return count;
//    }
    
    public int hammingWeight(int n) {
        int count=0;
        for(int i=0;i<32;i++){
        	System.out.println((n&(1<<i)));
            if((n&(1<<i))!=0) ++count;
        }
        return count;
    }
}
