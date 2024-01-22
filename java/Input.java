import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Input {

    public static void main(String[] args) throws IOException {
//        String result = string();
//        List<String> result = stringList();
//        int result = integer();
//        int[][] result = integer2dArray();
//        System.out.println("result is " + result);
    }

    // string
    public static String string() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        return br.readLine();
    }

    // string list
    public static List<String> stringList() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        List<String> stringList = new ArrayList<>();
        while (st.hasMoreTokens()) {
            stringList.add(st.nextToken());
        }
        return stringList;
    }

    // int
    public static int integer() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        return Integer.parseInt(br.readLine());
    }

    // int[][]
    public static int[][] integer2dArray() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st1.nextToken());
        int M = Integer.parseInt(st1.nextToken());
        int[][] array = new int[N][M];
        for (int i = 0; i < N; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                array[i][j] = Integer.parseInt(st2.nextToken());
            }
        }
        return array;
    }

}
