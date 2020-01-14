package Q2747;

import java.util.*;

public class Main {

	public static void main(String[] args) {
		int[] arr = new int[46];
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		arr[0] = 0;
		arr[1] = 1;
		for (int i = 2; i <= n; i++)
			arr[i] = arr[i - 1] + arr[i - 2];
		System.out.println(arr[n]);
		sc.close();
	}

}