package Q1748;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] num = new int[10];
        for (int i = 1; i < num.length; i++) {
            // i 자리수 숫자 개수 1~9, 10~99, 100~999 => 9, 90, 900
            num[i] = (int) (9 * Math.pow(10, i - 1));
        }
        int answer = 0;
        for (int i = 1; i < num.length; i++) {
            if (N > num[i]) {
                N -= num[i];
                answer += i * num[i];
            } else {
                answer += i * N;
                break;
            }
        }
        System.out.println(answer);
    }

}
