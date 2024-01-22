class Solution {
    public boolean isPalindrome(int x) {
        var input = String.valueOf(x).toCharArray();
        for (int i = 0; i < input.length; i++) {
            if (input[i] != input[input.length-1-i]) {
                return false;
            }
        }
        return true;
    }
}
