package books.concurrency_core.chap2.example14;

public class Run14_setNewStringTwoLock {
    public static void main(String[] args) throws InterruptedException {
        final Service service = new Service();
        Thread a = new Thread() {
            @Override
            public void run() {
                service.testMethod();
            }
        };
        a.setName("A");
        Thread b = new Thread() {
            @Override
            public void run() {
                service.testMethod();
            }
        };
        b.setName("B");

        a.start();
        // 给 a 线程时间来改变锁对象 lock
        Thread.sleep(50);
        b.start();

    }
}
