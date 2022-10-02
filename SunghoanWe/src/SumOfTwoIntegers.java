public class SumOfTwoIntegers {

	public int getSum(int a, int b) {
		int temp;
		while(b !=0) {
			temp = a^b;
			b = (a&b) << 1;
			a = temp;
		}
		return a;
        
    }
	
}
/*
a= 10
b= 11

a^b = 01
a&b = 10
*/