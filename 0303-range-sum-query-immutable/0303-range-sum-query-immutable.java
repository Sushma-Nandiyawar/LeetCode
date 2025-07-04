class NumArray {
    private int[] prefixArray;

    public NumArray(int[] nums) {
         int n = nums.length;
         prefixArray = new int[n];
         prefixArray[0] = nums[0];
         for (int i = 1; i<n; i++){
            prefixArray[i] = prefixArray[i-1] + nums[i];
         }
    }
    
    public int sumRange(int left, int right) {
        if(left==0) return prefixArray[right];
        return prefixArray[right] - prefixArray[left-1];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */