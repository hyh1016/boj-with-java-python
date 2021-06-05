package Q2167;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] array = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) array[i][j] = Integer.parseInt(st.nextToken());
        }

        int[][] dp = new int[n + 1][m + 1];
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) dp[i][j] = array[i-1][j-1] + (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]);
        }

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            int big_x = Math.max(x1, x2);
            int small_x = Math.min(x1, x2);
            int big_y = Math.max(y1, y2);
            int small_y = Math.min(y1, y2);
            System.out.println(dp[big_x][big_y] - dp[big_x][small_y-1] - dp[small_x-1][big_y] + dp[small_x-1][small_y-1]);
        }
    }

}
