class Solution(object):
    def generate(self, numRows):
        mainlist=[[1]]
        for i in range(numRows-1):
            temparray = [0] + mainlist[-1] + [0]
            row=[]
            for j in range(len(mainlist[-1])+1):
                row.append(temparray[j]+temparray[j+1])
            mainlist.append(row)
        return mainlist
        
        
        
        
        
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
