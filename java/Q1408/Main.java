package Q1408;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int current = parseSecond(br.readLine());
        int start = parseSecond(br.readLine());

        int result = 0;
        if (current > start) {
            int max = 24 * 3600;
            result = (max - current) + (start);
        } else result = start - current;

        int hour = result / 3600;
        int minute = (result - hour * 3600) / 60;
        int second = result - hour * 3600 - minute * 60;
        System.out.printf("%02d:%02d:%02d\n", hour, minute, second);
    }

    public static int parseSecond(String time) {
        String[] hms = time.split(":");
        return Integer.parseInt(hms[0]) * 3600
                + Integer.parseInt(hms[1]) * 60
                + Integer.parseInt(hms[2]);
    }

}
