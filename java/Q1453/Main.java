package Q1453;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        boolean[] seats = new boolean[101];
        int answer = 0;
        for (int i = 0; i < n; i++) {
            int current = Integer.parseInt(st.nextToken());
            if (seats[current]) answer++;
            else seats[current] = true;
        }
        System.out.println(answer);
    }

}
