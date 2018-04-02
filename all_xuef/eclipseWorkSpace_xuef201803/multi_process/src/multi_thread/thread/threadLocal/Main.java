package multi_thread.thread.threadLocal;

public class Main {
	public static void main(String[] args) {
//		Sequence seq = new SequenceA();
		
		Sequence seq = new SequenceB();
		
		ClientThread t1 = new ClientThread(seq);
		ClientThread t2 = new ClientThread(seq);
		ClientThread t3 = new ClientThread(seq);
		
		t1.start();
		t2.start();
		t3.start();
	}
}
