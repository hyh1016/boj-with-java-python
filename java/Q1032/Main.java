package Q1032;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] data = new String[n];
        for (int i = 0; i < n; i++) {
            data[i] = br.readLine();
        }
        String answer = "";
        for (int i = 0; i < data[0].length(); i++) {
            char c = data[0].charAt(i);
            boolean isSame = true;
            for (int j = 1; j < n; j++) {
                if (data[j].charAt(i) != c) {
                    isSame = false;
                    break;
                }
            }
            if (isSame) answer += c;
            else answer += '?';
        }
        System.out.println(answer);
    }

}
