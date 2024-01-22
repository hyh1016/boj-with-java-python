package Q2493;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] numbers = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        Stack<Integer> stack = new Stack<>();
        List<Integer> answer = new ArrayList<>();
        stack.push(0);
        answer.add(0);
        for (int i = 1; i < N; i++) {
            int n = numbers[i];
            while (!stack.isEmpty()) {
                if (numbers[stack.peek()] > n) break;
                stack.pop();
            }
            if (stack.isEmpty()) {
                answer.add(0);
            } else {
                answer.add(stack.peek()+1);
            }
            stack.push(i);
        }
        System.out.println(answer.stream().map(String::valueOf).collect(Collectors.joining(" ")));
    }

}
