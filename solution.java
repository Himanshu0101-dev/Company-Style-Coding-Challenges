import java.util.*;

public class BalancedWorkloadDistribution {

    public static int minDifference(int[] hours) {
        int totalSum = 0;

        for (int h : hours) {
            totalSum += h;
        }

        boolean[] dp = new boolean[totalSum + 1];
        dp[0] = true;

        for (int h : hours) {
            for (int s = totalSum; s >= h; s--) {
                dp[s] = dp[s] || dp[s - h];
            }
        }

        int minDiff = totalSum;

        for (int s = 0; s <= totalSum / 2; s++) {
            if (dp[s]) {
                minDiff = Math.min(minDiff, totalSum - 2 * s);
            }
        }

        return minDiff;
    }

    public static void main(String[] args) {
        int[] hours = {3, 1, 4, 2, 2};

        System.out.println(
            "Minimum Difference: " + minDifference(hours)
        );
    }
}
