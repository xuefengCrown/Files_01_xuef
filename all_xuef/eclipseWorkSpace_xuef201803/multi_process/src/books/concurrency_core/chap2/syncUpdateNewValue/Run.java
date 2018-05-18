package books.concurrency_core.chap2.syncUpdateNewValue;

/**
 * JVM -server 模式下运行
 * @author moveb
 */
public class Run {
	public static void main(String[] args) {
		try {
			Service service = new Service();
			ThreadA a = new ThreadA(service);
			a.start();
			Thread.sleep(1000);
			ThreadB b = new ThreadB(service);
			b.start();
			System.out.println("已经发起停止的命令了");
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
