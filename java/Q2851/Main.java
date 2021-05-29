package Q2851;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] scores = new int[10];
        for (int i = 0; i < 10; i++) scores[i] = Integer.parseInt(br.readLine());
        int answer = 0;
        for (int i : scores) {
            int newAnswer = answer + i;
            if (newAnswer <= 100) {
                answer = newAnswer;
                continue;
            }
            if (100 - answer >= newAnswer - 100) answer = newAnswer;
            break;
        }
        System.out.println(answer);
    }

}
