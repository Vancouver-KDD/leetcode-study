
def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x.start)

    for i in range(1, len(intervals)):
        if intervals[i].start < intervals[i-1].end:
            return False
    return True
