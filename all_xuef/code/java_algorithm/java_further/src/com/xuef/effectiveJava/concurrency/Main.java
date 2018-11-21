package com.xuef.effectiveJava.concurrency;

import java.util.HashSet;

public class Main {
	public static void main(String[] args) {
		ObservableSet<Integer> set = 
				new ObservableSet<>(new HashSet<Integer>());
		set.addOberver(new SetObserver<Integer>(){
			public void added(ObservableSet<Integer> s, Integer e){
				System.out.println(e);
				/**
				 * 企图在遍历列表的过程中，将一个元素从列表中删除，这是非法的！
				 */
				if(e == 23){
					s.rmObserver(this);
				}
			}
		});
		
		for(int i=0; i<100; i++){
			set.add(i);
		}
	}
}
