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
		
		// Àý»çÆò±Õ
		double sum = 0;
		for (int i = K; i < N - K; i++) {
			sum += ave.get(i);
		}
		System.out.printf("%.2f\n", sum / (N - 2 * K));

		// º¸Á¤Æò±Õ
		sum+=ave.get(K)*K;
		sum+=ave.get(N-K-1)*K;
		System.out.printf("%.2f\n", sum / N);
		
		sc.close();

	}

}
