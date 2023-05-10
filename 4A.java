import java.util.*;

public class watermelon {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();
        if (input%2==0 && input>2) {
            System.out.print("YES");
        } else {
            System.out.print("NO");
        }
    }
}
