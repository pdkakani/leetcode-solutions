class Solution {
    public int findJudge(int n, int[][] trust) {
        if (n==1) return 1;
        var trusted = new int[n+1];
        for (int[] ints : trust) {
            var zeroInd = ints[0];
            var firstInd = ints[1];
            trusted[zeroInd] = trusted[zeroInd] - 1;
            trusted[firstInd] = trusted[firstInd] + 1;
        }

        for (int i = 0; i < trusted.length; i++) {
            if (trusted[i] == n-1) {
                return i;
            }
        }
        return -1;

    }
}
