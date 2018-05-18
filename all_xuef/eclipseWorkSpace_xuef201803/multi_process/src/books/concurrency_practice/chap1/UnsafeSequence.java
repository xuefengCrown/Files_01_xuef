package books.concurrency_practice.chap1;
// not thread safe
public class UnsafeSequence {
	private int value;
	/** Returns a unique value. */
	public int getNext() {
		/**
		 * 需要考虑机器级执行细节
		 * 1. get value
		 * 2. value++
		 * 3. put value
		 */
		return value++;
	}
}
