class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0] )   #time_comp = O(nlogn)
        lst_intrvls = []
        first=intervals[0]
        
        for i in range(1,len(intervals)):
            if first[1] >= intervals[i][0]:
                first[1] = max(first[1], intervals[i][1])
            else:
                lst_intrvls.append(first)
                first = intervals[i]
        lst_intrvls.append(first)
        return lst_intrvls
    
       
        
        
        
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
