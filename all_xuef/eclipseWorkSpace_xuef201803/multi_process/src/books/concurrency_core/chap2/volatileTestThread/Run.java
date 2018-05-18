package books.concurrency_core.chap2.volatileTestThread;

public class Run {
	public static void main(String[] args) {
		MyThread[] myThreadArr = new MyThread[100];
		for(int i=0; i<100; i++){
			myThreadArr[i] = new MyThread();
		}
		for(int i=0; i<100; i++){
			myThreadArr[i].start();
		}
	}
}
