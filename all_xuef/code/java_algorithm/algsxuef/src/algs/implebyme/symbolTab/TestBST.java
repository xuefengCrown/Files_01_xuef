package algs.implebyme.symbolTab;

public class TestBST {

	public static void main(String[] args) {
		BST<String, Integer> bst = new BST();
		bst.put("S", 0);
		bst.put("E", 1);
		bst.put("A", 2);
		bst.put("R", 3);
		bst.put("C", 4);
		bst.put("H", 5);
		bst.put("E", 6);
		bst.put("X", 7);
		bst.put("A", 8);
		bst.put("M", 9);
		bst.put("P", 10);
		bst.put("L", 11);
		bst.put("E", 12);
		//bst.inorder();
		//System.out.println("min key: " + bst.min());
		for(String k:bst.keys()){
			System.out.print(k + ", ");
		}

		System.out.println();
		bst.levelorder();
	}

}
