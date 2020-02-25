/*
 * number : 2753
 * name : À±³â
*/
package Q2753;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int year = Integer.parseInt(br.readLine());
		int result=0;
		if(year%4==0) {
			if(year%100==0) {
				if(year%400==0)
					result=1;
			}
			else
				result=1;
		}
		System.out.println(result);
		br.close();
	}

}
