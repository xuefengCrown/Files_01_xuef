package multi_thread.thread.threadLocal;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class MyThreadLocal<T> {
	private Map<Thread, T> container = 
			Collections.synchronizedMap(new HashMap<Thread, T>());
	
	public void setValue(T value){
		container.put(Thread.currentThread(), value);
	}
	
	public T getValue(){
		Thread thread = Thread.currentThread();
		T value = container.get(thread);
		// 如果 container 中还没有这个 thread
		// 就调用 initialValue() 获得值
		if(value == null && !container.containsKey(thread)){
			value = initialValue();
			container.put(thread, value);
		}
		return value;
	}

	private T initialValue() {
		return null;
	}
	
	public void remove(){
		container.remove(Thread.currentThread());
	}
}
