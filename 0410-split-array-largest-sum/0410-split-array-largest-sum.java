class Solution {
    public int splitArray(int[] nums, int k) {
        int n = nums.length;
        int total = 0;
        int maxi = 0;
        for(int i=0; i<n; i++){
            total += nums[i];
            maxi = Math.max(maxi, nums[i]);
        }
        
        int start = maxi;
        int end = total;
        int mid = 0;
        int ans = 0;

        while(start <= end){
            mid = start + (end - start)/2;
            if(isValid(nums, mid, k)){
                ans = mid;
                end = mid - 1;
            }else{
                start = mid + 1;
            }
        }
        return ans;
    }

    public boolean isValid(int[] nums, int sum, int k){
        int subArrayCount = 1;
        int count = 0;
        for(int i=0; i<nums.length; i++){
            if(count + nums[i] > sum){
                subArrayCount++;
                count = 0;
            }
            count += nums[i];
            if(subArrayCount > k) return false;
        }
        return true;
    }
}