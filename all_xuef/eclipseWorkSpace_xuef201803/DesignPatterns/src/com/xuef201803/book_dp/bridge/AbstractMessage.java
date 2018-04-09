package com.xuef201803.book_dp.bridge;

public abstract class AbstractMessage {
	/**
	 * 持有一个实现部分的对象
	 */
	protected MessageImplementor messageImpl;

	public AbstractMessage(MessageImplementor messageImpl) {
		this.messageImpl = messageImpl;
	}
	
	/**
	 * 发送消息，转调实现部分的方法
	 * @param message
	 * @param toUser
	 */
	public void sendMessage(String message, String toUser){
		this.messageImpl.send(message, toUser);
	}
}
