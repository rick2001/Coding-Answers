class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        Jobs.sort(key=lambda x:x.profit, reverse=True)
        # T.C-> O(N^2)
        # S.C-> O(N)
        
        maxDeadLine=0
        for i in range(n):
            maxDeadLine = max(maxDeadLine, Jobs[i].deadline)
        arr = [-1]*maxDeadLine
        profit=0
        count=0
        for i in range(n):
            for j in range(Jobs[i].deadline, 0, -1):
                if arr[j-1]==-1:
                    arr[j-1]=Jobs[i].id
                    profit+=Jobs[i].profit
                    count+=1
                    break
        return [count,profit]
