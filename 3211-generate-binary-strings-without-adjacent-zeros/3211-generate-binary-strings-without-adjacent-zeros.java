class Solution {
    public List<String> validStrings(int n) {
        List<String> ans=new ArrayList<>();
        helper(ans,n,new StringBuilder());
        return ans;
    }
    public static void helper(List<String> ans,int n,StringBuilder str){
        if(n==0){
            ans.add(str.toString());
            return;
        }
        if((str.length()==0) || (str.charAt(str.length()-1)=='1')){
            str.append('0');
            helper(ans,n-1,str);
            str.deleteCharAt(str.length()-1);
        }
        str.append('1');
        helper(ans,n-1,str);
        str.deleteCharAt(str.length()-1);
    }
}