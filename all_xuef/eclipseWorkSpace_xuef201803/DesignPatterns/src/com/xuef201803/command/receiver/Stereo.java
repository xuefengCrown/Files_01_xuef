package com.xuef201803.command.receiver;
/**
 * ����ӿ�
 * @author moveb
 */
public interface Stereo {
	public void on();
	public void off();
	/**
	 * ���óɲ���CD
	 */
	public void setCd();
	public void setDvd();
	public void setRadio();
	/**
	 * ��������
	 * @param volume
	 */
	public void setVolume(int volume);
}