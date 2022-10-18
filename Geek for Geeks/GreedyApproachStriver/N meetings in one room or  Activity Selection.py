#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        
        # T.C-> O(N) for adding + O(NlogN) for sorting + O(N) for Traversing,checking & adding
        # Ultimate it is -> O(NlogN)
        # S.C-> O(N)
        
         #creating new Array
        newArray=[]
        for i in range(n):
            newArray.append([start[i], end[i], i+1])
        
        # sorting newArray
        newArray.sort(key=lambda x : x[1])
        # print(newArray)
        
        # performing the actual operation
        newAnsArray=[]
        newAnsArray.append(newArray[0][2])
        limit=newArray[0][1]
        
        for i in range(1,len(newArray)):
            if newArray[i][0]>limit:
                limit = newArray[i][1]
                newAnsArray.append(newArray[i][2])
        return len(newAnsArray)
