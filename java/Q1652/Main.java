package Q1652;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static int n;
    private static char[][] room;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        room = new char[n][n];
        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            for (int j = 0; j < n; j++) room[i][j] = input.charAt(j);
        }
        int row = 0;
        int column = 0;
        for (int i = 0; i < n; i++) {
            row += getCount(i, -1);
            column += getCount(-1, i);
        }
        System.out.println(row + " " + column);
    }

    public static int getCount(int row, int column) {
        String string = "";
        if (column == -1) for (int j = 0; j < n; j++) string += room[row][j];
        if (row == -1) for (int j = 0; j < n; j++) string += room[j][column];
        String[] candidate = string.split("X");
        int count = 0;
        for (String c : candidate) if (c.length() >= 2) count++;
        return count;
    }

}
