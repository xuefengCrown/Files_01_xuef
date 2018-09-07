package algs.implebyme;

import algs.base.StdOut;

public class RingBufefrTest {
	public static void main(String[] args) {
		RingBuffer<String> rb = new RingBuffer<>(5);
		//StdOut.println(rb.dequeue());
		rb.enqueue("aa");
		rb.enqueue("bb");
		rb.enqueue("cc");
		StdOut.println(rb.dequeue());
		rb.enqueue("dd");
		rb.enqueue("ff");
		//此处是单线程，因为队列满了，所以下面数据就丢失了。
		//在现实中，应是多线程。生产者见缓存区满了，应该等待消费者消费掉一部分缓冲区元素后再存入。
		rb.enqueue("yy");
		rb.enqueue("11");
		rb.enqueue("22");
		rb.enqueue("33");
		rb.enqueue("44");
		rb.enqueue("55");
		rb.enqueue("66");
		StdOut.println(rb.dequeue());
		StdOut.println(rb.dequeue());
		StdOut.println(rb.dequeue());
		StdOut.println(rb.dequeue());
		rb.enqueue("77");
		rb.enqueue("88");
		rb.enqueue("99");
		StdOut.println(rb.dequeue());
		StdOut.println(rb.dequeue());
		StdOut.println(rb.dequeue());
		StdOut.println(rb.dequeue());
	}
}
