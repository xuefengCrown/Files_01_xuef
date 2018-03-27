package com.xuef.ssm.domain;

import java.util.HashMap;
import java.util.Map;

/**
 * ��װ�������ݺ���Ϣ
 * @author moveb
 */
public class ResWithMSG {
	// ״̬�� 0:ʧ�� 1:�ɹ�
	private int status;
	// ��ʾ��Ϣ
	private String msg;
	private Map<String, Object> res = new HashMap();
	
	public static ResWithMSG success(){
		ResWithMSG resWithMSG = new ResWithMSG();
		resWithMSG.setStatus(1);
		resWithMSG.setMsg("success");
		
		return resWithMSG;
	}

	public static ResWithMSG fail(){
		ResWithMSG resWithMSG = new ResWithMSG();
		resWithMSG.setStatus(0);
		resWithMSG.setMsg("fail");
		return resWithMSG;
	}
	public ResWithMSG add(String key, Object data){
		this.res.put(key, data);
		return this;
	}
	public int getStatus() {
		return status;
	}

	public void setStatus(int status) {
		this.status = status;
	}

	public String getMsg() {
		return msg;
	}

	public void setMsg(String msg) {
		this.msg = msg;
	}

	public Map<String, Object> getRes() {
		return res;
	}

	public void setRes(Map<String, Object> res) {
		this.res = res;
	}

	@Override
	public String toString() {
		return "ResWithMSG [status=" + status + ", msg=" + msg + ", res=" + res
				+ "]";
	}
	
}