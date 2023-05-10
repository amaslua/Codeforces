import java.util.*;

public class nextround {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        int output = 0;
        for (int i = 0; i < k-1; i++) {
           int next = scanner.nextInt();
           if (next > 0) output += 1;
        }
        int pointer = scanner.nextInt();
        if (pointer > 0) output += 1;
        for (int j = 0; j < n-k; j++) {
            int cur = scanner.nextInt();
            if (cur == pointer && cur > 0) output += 1;
        }
        scanner.close();
        System.out.println(output);
    }
}