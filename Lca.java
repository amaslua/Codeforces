/**
 * Name         : Amas Lua Yong Da
 * Matric. No   : A0199368E
*/

import java.util.*;

public class Lca {
    public class Node {
        Node left, right, parent;
        int index, value;

        public Node(int val, int in) {
            this.left = this.right = this.parent = null;
            this.index = in;
            this.value = val;
        }

        public void setLeft(Node n) {
            this.left = n;
            n.parent = this;
        }

        public void setRight(Node n) {
            this.right = n;
            n.parent = this;
        }
    }
    
    public int lca(Node[] nodes, Node a, Node b) {
        Node cur = nodes[0];
        while (true) {
            System.out.println(cur);
            int val = cur.value;
            int ind = cur.index;
            if (cur.value >= a.value && cur.value <= b.value) {
                break;
            }
            if (cur.value<a.value) {
                cur = cur.right;
            } else {
                cur = cur.left;
            }
        }
        return cur.index+1;
    }

    private void run() {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        int moves = scanner.nextInt();
        Node[] nodes = new Node[number];
        for (int i = 0; i < number; i++) {
            nodes[i] = new Node(scanner.nextInt(), i);
        }
        for (int j = 0; j < number-1; j++) {
            String move = scanner.next();
            int p = scanner.nextInt()-1;
            int c = scanner.nextInt()-1;
            if (move.equals("L")) {
                nodes[p].setLeft(nodes[c]);
            } else {
                nodes[p].setRight(nodes[c]);
            }
        }
        for (int k = 0; k < moves; k++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            Node nodeA = nodes[a-1];
            Node nodeB = nodes[b-1];
            if (a > b) {
                int output = lca(nodes, nodeB, nodeA);
                System.out.println(output);
            } else {
                int output = lca(nodes, nodeA, nodeB);
                System.out.println(output);
            }
        }
        scanner.close();
    }

    public static void main(String args[]) {
        Lca runner = new Lca();
        runner.run();
    }
}
