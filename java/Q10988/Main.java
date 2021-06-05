package Q10988;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        int left = 0;
        int right = word.length()-1;
        int answer = 1;
        while (left <= right) {
            if (word.charAt(left) != word.charAt(right)) {
                answer = 0;
                break;
            }
            left++;
            right--;
        }
        System.out.println(answer);
    }

}
