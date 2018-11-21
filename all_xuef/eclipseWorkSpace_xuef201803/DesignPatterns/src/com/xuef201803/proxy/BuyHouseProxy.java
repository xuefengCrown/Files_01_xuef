package com.xuef201803.proxy;
/**
 * 代理类
 * @author moveb
 * 2018.10.25
 * 缺点：我们得为每一个服务都得创建代理类，工作量太大，不易管理。
 * 同时接口一旦发生改变，代理类也得相应修改。
 */
public class BuyHouseProxy implements BuyHouse {
	BuyHouse buyHouse; // 被代理对象，即委托者
	public BuyHouseProxy(final BuyHouse buyHouse) {
		this.buyHouse = buyHouse;
	}
	@Override
	public void buyHouse() {
		before();
		buyHouse.buyHouse();
		after();
	}

	void before(){
		System.out.println("before...");
	}
	
	void after(){
		System.out.println("after...");
	}
}
