package com.xuef201803.book_dp.bridge;

public class MessageMobile implements MessageImplementor {
	@Override
	public void send(String message, String toUser) {
		System.out.println("以手机短消息的方式发送消息： " + message + 
				" 给 " + toUser);
	}
}
