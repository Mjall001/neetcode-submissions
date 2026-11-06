"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        #two pointers one on 1st another on 2nd
        #save start and end
        #if end2 < end1 or end1 < start1 return false
        
        for i,v in enumerate(intervals): #0,0-30
            for j in range(i+1,len(intervals)):#1
                if v.start <= intervals[j].start < v.end or v.start<=intervals[j].end <=v.end:
                    return False
        
        return True
