package com.xuef201803.command.receiver;
/**
 * 音响接口
 * @author moveb
 */
public interface Stereo {
	public void on();
	public void off();
	/**
	 * 设置成播放CD
	 */
	public void setCd();
	public void setDvd();
	public void setRadio();
	/**
	 * 设置音量
	 * @param volume
	 */
	public void setVolume(int volume);
}
