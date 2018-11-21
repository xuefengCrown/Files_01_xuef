package multiprocess_core.service;

public class HasSelfPrivateNum {
	private int num = 0;
	/**
	 * synchronized 获得的锁都是对象锁，哪个线程先进入同步代码块，其他线程
	 * 就只能等待，但前提是多个线程访问的是同一个对象。
	 * @param uname
	 */
	synchronized public void addI(String uname){
		
		try{
			if(uname.equals("a")){
				num = 100;
				System.out.println("a set over");
				Thread.sleep(2000);
			}else{
				num  = 200;
				System.out.println("b set over");
			}
			System.out.println(uname + " num = " + num);
		} catch(InterruptedException ie){
			ie.printStackTrace();
		}
	}
}
