import java.util.*;
import java.util.function.UnaryOperator;
public class a
{
    static int[] cumsum;
    static int[] arr = {1,2,3,4,5,6};

    public a(ArrayList<Integer> input)
    {
        for (int i = 0; i < input.size(); i++) {
            arr[i] = input.get(i);
        }
    }
    
    public static void get(int[] q, UnaryOperator<Integer> f)
    {
        cumsum = new int[q.length+1];
        cumsum[0] = 0;
        for (int j = 1; j < q.length+1; j++) {
            cumsum[j] = cumsum[j-1]+f.apply(q[j-1]);
        }
    }
    
    public static void main (String args[]) {
        get(arr, u -> u*u);
        for (int k = 0; k < cumsum.length; k++) {
            System.out.println(cumsum[k]);
        }
    }
}