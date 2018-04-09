package com.xuef201803.book_dp.factoryByReflect;

import com.xuef201803.book_dp.simpleFactory.Api;

public class Client {
	public static void main(String[] args) {
		Api instance = FactoryByReflect.getInstance();
		instance.operate();
	}
}
