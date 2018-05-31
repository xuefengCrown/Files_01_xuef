package multi_thread.thread.threadLocal;

/**
 * ʹ�� ThreadLocal(��������Ϊһ�����������ڴ���̵߳ľֲ�����)
 * 
 * @author moveb
 */
public class SequenceB implements Sequence {
	// ÿ���߳̿�ӵ���Լ��� static ����
	private static ThreadLocal<Integer> numContainer =
						new ThreadLocal<Integer>(){
							@Override
							protected Integer initialValue(){
								return 0;
							}
						};
	
	@Override
	public int getNumber() {
		numContainer.set(numContainer.get() + 1);
		return numContainer.get();
	}
}