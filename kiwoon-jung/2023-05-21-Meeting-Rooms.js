export class Solution {
  /**
   * @param intervals: an array of meeting time intervals
   * @return: if a person could attend all meetings
   */
  canAttendMeetings(intervals) {
    // Write your code here
    const times = new Set();

    for (let i = 0; i < intervals.length; i += 1) {
      for (let j = intervals[i][0]; j < intervals[i][1]; j += 1) {
        if (times.has(j)) {
          return false;
        } else {
          times.add(j);
        }
      }
    }

    return true;
  }
}
