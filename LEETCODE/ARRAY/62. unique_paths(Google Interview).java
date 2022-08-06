class Solution {
    public int uniquePaths(int m, int n) {
        int N = m+n-2;
        int R=m-1;       //we can use either m-1 or n-1
        double result = 1;
        for (int i=1; i<=R; i++){
            result= (result*(N-R+i))/i;
        }
        return (int)result;
        
    }
}
