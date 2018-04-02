package multi_thread.thread.threadLocal;

/**
 * 一个序列号生成器，可能会有多个线程并发访问它;
 * 要保证每个序列号得到的序列号都是自增的，互不干扰。
 * @author moveb
 */
public interface Sequence {
	public int getNumber();
}
