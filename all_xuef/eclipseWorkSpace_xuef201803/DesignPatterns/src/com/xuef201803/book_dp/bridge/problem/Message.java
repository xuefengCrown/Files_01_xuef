package com.xuef201803.book_dp.bridge.problem;

/**
 * ��Ϣ��ͳһ�ӿ�
 * @author moveb
 */
public interface Message {
	/**
	 * ������Ϣ
	 * @param message Ҫ���͵���Ϣ
	 * @param toUser ����Ŀ����
	 */
	public void send(String message, String toUser);
}