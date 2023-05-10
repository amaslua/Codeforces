import java.util.*;

public class bit {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int out = 0;
        for (int i = 0; i < n; i++) {
            String next = scanner.next();
            if (next.charAt(1) == '+') {
                out++;
            } else {
                out--;
            }
        }
        System.out.println(out);
    }
}