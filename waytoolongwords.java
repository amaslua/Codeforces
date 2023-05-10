import java.util.*;

public class waytoolongwords {
    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numberWords = scanner.nextInt();
        for (int i = 0; i < numberWords; i++) {
            String word = scanner.next();
            if (word.length() <= 10) {
                System.out.println(word);
            } else {
                int middle = word.length()-2;
                System.out.printf("%s%d%s\n", word.charAt(0), middle, word.charAt(word.length()-1));
            }
        }
    }
}
