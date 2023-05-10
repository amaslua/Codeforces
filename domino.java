import java.util.*;

public class domino {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        scanner.close();
        int out = 0;
        if (a % 2 == 0) {
            out = a / 2 * b;
        } else if (b % 2 == 0) {
            out = b / 2 * a;
        } else {
            int big = Math.max(a, b);
            int small = Math.min(a, b);
            out += (big - 1) / 2 * small;
            out += (small - 1) / 2;
        }
        System.out.println(out);
    }
}
