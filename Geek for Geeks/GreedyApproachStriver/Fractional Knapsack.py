class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        
        # T.C- O(NlogN)+O(N)
        # S.C- O(N)
        
        arr=[]
        # index->0 is Value/weight & index-1-> value & index-2 -> weight
        for i in range(n):
            arr.append([Items[i].value/Items[i].weight, Items[i].value,  Items[i].weight])
        arr.sort(key=lambda x:x[0], reverse=True)
        currentWeight=0
        profit=0
        for j in range(n):
            if (currentWeight+arr[j][2]) <= W:
                currentWeight+=arr[j][2]
                profit+=arr[j][1]
            else:
                remain = W - currentWeight
                profit+= arr[j][0]*remain
                break
        return profit
