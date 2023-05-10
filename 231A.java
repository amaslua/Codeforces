import java.util.*;

public class team {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        int output = 0;
        for (int i = 0; i < number; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int c = scanner.nextInt();
            if (a+b+c >= 2) output += 1;
        }
        System.out.print(output);
    }
}