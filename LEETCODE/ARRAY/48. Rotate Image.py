#Python solution

class Solution(object):
    def rotate(self, matrix):
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for k in range(len(matrix)):
            matrix[k].reverse()
        return 

#java solution

class Solution {
    public void rotate(int[][] matrix) {
        for(int i=0; i<matrix.length; i++){
            for(int j=i; j<matrix[0].length; j++){
                int temp=matrix[i][j];
                matrix[i][j]=matrix[j][i];
                matrix[j][i]=temp;
            }
        }
        reverse(matrix);
    }
    
    public void reverse(int[][] array){
        for(int i=0; i<array.length; i++){
            int start=0;
            int end=array[i].length-1;
            
            while(start<=end){
                int temp=array[i][start];
                array[i][start]= array[i][end];
                array[i][end]=temp;
                
                start++;
                end--;
            }
        }
    }
}
