class Solution {
    public int totalFruit(int[] fruits) {
        int last_fr = -1;
        int second_last_fr = -1;
        int last_fr_count = 0;
        int current_max = 0;
        int max = 0;

        for(Integer fruit : fruits){

            if(fruit == last_fr || fruit == second_last_fr){
                current_max +=1;
            }else{
                current_max = last_fr_count +1;
            }

            if(fruit == last_fr){
                last_fr_count += 1;
            }else{
                last_fr_count = 1;
            }

            if(fruit != last_fr){
                second_last_fr = last_fr;
                last_fr = fruit;
            }
            max = Math.max(current_max, max);
        }
        return max;
    }
}