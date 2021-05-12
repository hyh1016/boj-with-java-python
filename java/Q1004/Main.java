package Q1004;

import java.util.Scanner;

class Point {
    int x;
    int y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Circle extends Point {
    int r;

    Circle(int x, int y, int r) {
        super(x, y);
        this.r = r;
    }

    boolean includePoint(Point p) {
        int distance = (p.x - x) * (p.x - x) + (p.y - y) * (p.y - y);
        return (distance > r * r);
    }

}

public class Main {

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int i = 0; i < T; i++) {
            Point p1 = new Point(sc.nextInt(), sc.nextInt());
            Point p2 = new Point(sc.nextInt(), sc.nextInt());
            int n = sc.nextInt();
            int count = 0;
            for (int j = 0; j < n; j++) {
                Circle c = new Circle(sc.nextInt(), sc.nextInt(), sc.nextInt());
                if (c.includePoint(p1) ^ c.includePoint(p2))
                    count++;
            }
            System.out.println(count);
        }
        sc.close();
    }

}