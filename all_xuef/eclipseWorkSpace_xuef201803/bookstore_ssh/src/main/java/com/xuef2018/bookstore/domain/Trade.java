package com.xuef2018.bookstore.domain;

import java.util.Date;

public class Trade {
	private int tradeid;
	private int userid;
	private Date tradetime;
	public int getTradeid() {
		return tradeid;
	}
	public void setTradeid(int tradeid) {
		this.tradeid = tradeid;
	}
	public int getUserid() {
		return userid;
	}
	public void setUserid(int userid) {
		this.userid = userid;
	}
	public Date getTradetime() {
		return tradetime;
	}
	public void setTradetime(Date tradetime) {
		this.tradetime = tradetime;
	}
	@Override
	public String toString() {
		return "Trade [tradeid=" + tradeid + ", userid=" + userid
				+ ", tradetime=" + tradetime + "]";
	}
	
}
