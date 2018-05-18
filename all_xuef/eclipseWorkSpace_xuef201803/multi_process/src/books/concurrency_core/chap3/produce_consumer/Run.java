package books.concurrency_core.chap3.produce_consumer;

public class Run {
	public static void main(String[] args) {
		String lock = new String("");
		Produce p = new Produce(lock);
		Consumer c = new Consumer(lock);
		ThreadP pTh = new ThreadP(p);
		ThreadC cTh = new ThreadC(c);
		pTh.start();
		cTh.start();
	}
}
