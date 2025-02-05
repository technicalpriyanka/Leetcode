class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        if(s1.equals(s2)){
            return true;
        }
        int arr[]=new int[2];
        int a=0;
        for(int i=0;i<s1.length();i++){
            if(s1.charAt(i)!=s2.charAt(i)){
                if(a>=2){
                    return false;
                }
                arr[a]=i;
                a++;
            }
        }
        if(a!=2){
            return false;
        }
        return (s1.charAt(arr[0])==s2.charAt(arr[1]) && 
        s1.charAt(arr[1])==s2.charAt(arr[0]));
    }
}