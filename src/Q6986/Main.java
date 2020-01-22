/*
 * number : 6986
 * name : Àý»çÆò±Õ
*/
package Q6986;

import java.util.Scanner;
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		ArrayList<Double> ave = new ArrayList<>(N);

		for (int i = 0; i < N; i++) {
			ave.add(sc.nextDouble());
		}

		ave.sort(null);

		double sum = 0;
		// Àý»çÆò±Õ
		for (int i = K; i < N - K; i++) {
			sum += ave.get(i);
		}
		System.out.printf("%.2f\n", sum / (N - 2 * K));

		sum = 0;
		// º¸Á¤Æò±Õ
		for (int i = 0; i < N; i++) {
			if (i < K)
				sum += ave.get(K);
			else if (i > N - K - 1)
				sum += ave.get(N - K - 1);
			else
				sum += ave.get(i);
		}
		System.out.printf("%.2f\n", sum / N);

	}

}
