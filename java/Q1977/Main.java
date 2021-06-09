package Q1977;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());
        int min_sqrt = (int) Math.ceil((Math.sqrt(m)));
        int max_sqrt = (int) Math.floor((Math.sqrt(n)));
        int sum = 0;
        for (int i = min_sqrt; i <= max_sqrt; i++) {
            sum += i * i;
        }
        if (sum == 0) System.out.println(-1);
        else {
            System.out.println(sum);
            System.out.println(min_sqrt * min_sqrt);
        }
    }

}
