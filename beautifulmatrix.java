import java.util.Scanner;

public class beautifulmatrix {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                int n = scanner.nextInt();
                if (n == 1) {
                    int out = Math.abs(i - 2) + Math.abs(j - 2);
                    System.out.println(out);
                }
            }
        }
    }
}