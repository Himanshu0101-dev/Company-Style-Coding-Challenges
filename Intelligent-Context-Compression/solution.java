public class Main {

    public static int longestContext(long[] tokens, long K) {

        int left = 0;
        long sum = 0;
        int answer = 0;

        for (int right = 0; right < tokens.length; right++) {

            sum += tokens[right];

            while (sum > K) {
                sum -= tokens[left];
                left++;
            }

            answer = Math.max(answer,
                    right - left + 1);
        }

        return answer;
    }

    public static void main(String[] args) {

        long[] tokens =
                {120, 80, 150, 100, 50};

        long K = 300;

        System.out.println(
                longestContext(tokens, K));
    }
}
