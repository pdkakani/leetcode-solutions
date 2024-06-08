class Solution {
    public int longestConsecutive(int[] nums) {
        int ans = 0;
        var hashSet = new HashSet<Integer>();

        for (int i = 0; i < nums.length; i++) {
            hashSet.add(nums[i]);
        }

        for (int i = 0; i < nums.length; i++) {
            if (!hashSet.contains(nums[i] - 1)) {
                int count = 0;
                int j = nums[i];
                while (hashSet.contains(j)) {
                    hashSet.remove(j);
                    count++;
                    j++;
                }
                ans = Math.max(ans, count);

            }
        }
        return ans;
    }
}
