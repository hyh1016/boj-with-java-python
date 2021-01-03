/*
 * number : 1010
 * name : 다리 놓기
*/
package Q1010;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static long com(int n, int r) {
		if(n==r)
			return 1;
		if(r==1)
			return n;
		else
			return (com(n-1, r)+com(n-1, r-1));
	}
	
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());

		for (int i = 0; i < T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			
			//Overflow 발생
			//double은 오차 발생이 잦으므로 정수 계산 시 이용하면 안 됨
			/*double result = 1;
			for (int j = M; j > N; j--) {
				result *= j;
				result /= (j - N);
			}*/

			System.out.println(com(M, N));
		}
		br.close();
	}
}
