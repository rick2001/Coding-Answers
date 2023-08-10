class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        //intuition is we will start from arr[0][4] value as in desc it is mentioned that values are row wise and column wise sorted. 
       // So if here we consider 15, on the left side of 15 all values are less, and below 15 all values are greater. 
       // so if the target value is less so we will change the column else if it is big we will change the row. 
       // in that way we can find the element.
        
        int row=0;
        int column=matrix[0].length-1;
        
        while(row<matrix.length && column>=0){
            if(matrix[row][column]==target){
                return true;
            }
            else if(target < matrix[row][column]){
                column--;
            }
            else{
                row++;
            }
        }
        return false;
    }
}
