package multi_thread.thread.safe.extthread;

public class Test3 {
	public static void main(String[] args) {
		Alogin al = new Alogin();
		al.start();
		Blogin bl = new Blogin();
		bl.start();
	}
}
