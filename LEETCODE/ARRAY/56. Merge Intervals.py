#best solution / optimal approach
# O(nLogN)+O(N)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ansArray=[]
        for i in range(len(intervals)):
            if len(ansArray)==0 or intervals[i][0]>ansArray[-1][1]:
                ansArray.append(intervals[i])
            else:
                ansArray[-1][1]=max(ansArray[-1][1], intervals[i][1])
        return ansArray





# bruteforce solution   O(nlogN)+O(2N) soring + adding into 

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         # bruteforce solution   O(nlogN)+O(2N) soring + adding into 
#         intervals.sort(key=lambda x:x[0])
#         ansArray=[]
#         for i in range(len(intervals)):
#             start=intervals[i][0]
#             end=intervals[i][1]
#             if (len(ansArray)!=0 and end <= ansArray[-1][1]): #this condition is basically to skip the array elemts which are already present in the ansArray
#                 continue
            
#             for j in range(i+1, len(intervals)):   #this loop is to check the add the intervals 
#                 if intervals[j][0] <= end:
#                     end=max(end,intervals[j][1])
#                 else:
#                     break
#             ansArray.append([start, end])
#         return ansArray
