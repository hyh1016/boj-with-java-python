package Q1003;

import java.util.Scanner;

public class Main {

    public static void main(String args[]) {
        int[] arr = new int[41];
        int[] count0 = new int[41];
        int[] count1 = new int[41];
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        arr[0] = 0;
        arr[1] = 1;
        count0[0] = 1;
        count1[1] = 1;
        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            for (int j = 2; j <= n; j++) {
                count0[j] = count0[j - 1] + count0[j - 2];
                count1[j] = count1[j - 1] + count1[j - 2];
            }
            System.out.println(count0[n] + " " + count1[n]);
        }
        sc.close();
    }

}
