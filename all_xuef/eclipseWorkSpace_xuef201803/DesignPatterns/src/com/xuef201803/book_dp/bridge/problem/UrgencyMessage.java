package com.xuef201803.book_dp.bridge.problem;

/**
 * �Ӽ���Ϣ�ĳ���ӿ�
 * @author moveb
 *
 */
public interface UrgencyMessage extends Message {

	/**
	 * ���ĳ��Ϣ�Ĵ�������
	 * @param messageId �������Ϣ�ı��
	 * @return
	 */
	public Object watch(String messageId);
}