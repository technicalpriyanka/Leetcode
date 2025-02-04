class Solution {
    public boolean isArraySpecial(int[] arr) {
        int L=0;
        int pairs=arr.length-1;
        for(int R=L+1;R<arr.length;R++){
            if((arr[L]%2==0 && arr[R]%2!=0)||(arr[L]%2!=0 && arr[R]%2==0)){
                pairs-=1;
                L++;
            }else{
                return false;
            }
        }
        
        return pairs==0;
        
    }
}