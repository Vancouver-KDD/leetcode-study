class Solution{
    public boolean canAttendMeeting(Interval[] intervals){
        Arrays.sort(intervals, new Comparator<Interval>(){
            public int compare(Interval i1, Interval i2){
                return i1.strat -i2.start;
            }
        });
        Interval last = null;
        for(Interval i: intervals){
            if(last != null&& i.start < last.end){
                return false;
            }
            last = i;
        }
        return true;
    }
}