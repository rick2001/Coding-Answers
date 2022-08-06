class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0){
            return false;
        }
        int row = matrix.length;
        int column = matrix[0].length;
        
        int low = 0;
        int high = (row*column)-1;
        
        boolean flag = false;
        while (low <= high){
            int mid = (low+high)/2;
            if(matrix[mid/column][mid%column]==target){
                return true;
            }
            else if (target < matrix[mid/column][mid%column]){
                high = mid-1;
            }
            else{
                low = mid+1;
            }
        }
        return flag;
        
    }
}

