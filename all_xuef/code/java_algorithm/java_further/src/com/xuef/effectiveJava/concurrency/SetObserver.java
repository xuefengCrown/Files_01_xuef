package com.xuef.effectiveJava.concurrency;

public interface SetObserver<E> {
	// invoke when an element is added to the onservable set
	void added(ObservableSet<E> set, E ele);
}
