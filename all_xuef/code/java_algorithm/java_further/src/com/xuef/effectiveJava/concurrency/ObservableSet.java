package com.xuef.effectiveJava.concurrency;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

import com.xuef.effectiveJava.class_and_interface.ForwardingSet;

/**
 * Broken - invoke alien method from synchronized block!
 * @author moveb
 *
 * @param <E>
 */
public class ObservableSet<E> extends ForwardingSet<E> {

	public ObservableSet(Set<E> s) {
		super(s);
	}
	// ∂©‘ƒ’ﬂ, π€≤Ï’ﬂ
	private final List<SetObserver<E>> observers = new ArrayList<>();
	
	public void addOberver(SetObserver<E> ob){
		synchronized (observers) {
			observers.add(ob);
		}
	}
	public boolean rmObserver(SetObserver<E> ob){
		synchronized (observers) {
			return observers.remove(ob);
		}
	}
	private void notifyAllObserver(E ele){
		synchronized (observers) {
			for(SetObserver<E> observer : observers){
				observer.added(this, ele);
			}
		}
	}
	@Override
	public boolean add(E ele){
		boolean added = super.add(ele);
		if(added){
			notifyAllObserver(ele);
		}
		return added;
	}
	
}
