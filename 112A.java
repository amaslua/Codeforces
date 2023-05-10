import java.util.*;

public class petya {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String i = sc.next();
        String j = sc.next();
        i = i.toLowerCase();
        j = j.toLowerCase();
        int diff = i.compareTo(j);
        if (diff > 0) {
            System.out.println(1);
        } else if (diff == 0) {
            System.out.println(0);
        } else {
            System.out.println(-1);
        }
    }
}
