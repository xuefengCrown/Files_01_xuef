package multi_thread.thread.safe.extobject;
/**
 * 验证 同步锁是对象锁
 * @author moveb
 *
 */
public class Run {
	public static void main(String[] args) {
		MyObject obj = new MyObject();
		ThreadA ta = new ThreadA(obj);
		ta.setName("a");
		ThreadB tb = new ThreadB(obj);
		tb.setName("b");
		
		ta.start();
		tb.start();
	}
}
