/*
 * number : 1004
 * name : 어린 왕자
*/
package Q1004;

import java.util.Scanner;

class Point {
	int x; // x좌표
	int y; // y좌표

	Point(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

class Circle extends Point {
	int r; // 반지름 길이

	Circle(int x, int y, int r) {
		super(x, y);
		this.r = r;
	}

	boolean includePoint(Point p) {
		int distance = (p.x-x)*(p.x-x) + (p.y-y)*(p.y-y);
		return (distance > r*r); //제곱근을 구하는 것보다 제곱값을 비교해주는 것이 더 편함
	}

}

public class Main {

	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt(); //테스트 케이스 개수
		
		for(int i=0; i<T; i++) {
			
			Point p1 = new Point(sc.nextInt(),sc.nextInt()); //출발점
			Point p2 = new Point(sc.nextInt(),sc.nextInt()); //도착점
			
			int n=sc.nextInt(); //행성 수
			
			int count=0;
			for(int j=0;j<n;j++) {
				Circle c = new Circle(sc.nextInt(), sc.nextInt(), sc.nextInt());
				if(c.includePoint(p1) ^ c.includePoint(p2)) //★모든 경우를 고려하는 것의 중요성
					count++;
			}
			System.out.println(count);
			
		}
		
		sc.close();
	} //out main

}