package com.xuef201803.book_dp.bridge;
/**
 * 发送消息的统一接口
 * @author moveb
 *
 */
public interface MessageImplementor {
	/**
	 * 发送消息
	 * @param message
	 * @param toUser
	 */
	public void send(String message, String toUser);
}
