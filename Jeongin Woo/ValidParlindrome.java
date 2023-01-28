import java.util.Stack;

public class ValidParlindrome {
	   public boolean isPalindrome(String s) {
		   Stack stack = new Stack();
			
			 String strNew = s.replace(" ", "");

				 
			 for(int i =0;i< strNew.length();i++)
			 {
				
				 stack.push(strNew.charAt(i));	
		 
			 }
			 
			 String reverseS = "";
			 
			 while(!stack.isEmpty())
			{
			
				 reverseS = reverseS+stack.pop();
					                                        
			}
			 if(strNew.equals(reverseS))
				 return true;
			 else
				 return false;

	    }
}
