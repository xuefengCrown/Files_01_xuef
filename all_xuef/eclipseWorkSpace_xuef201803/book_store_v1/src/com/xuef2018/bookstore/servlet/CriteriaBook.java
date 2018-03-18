package com.xuef2018.bookstore.servlet;

public class CriteriaBook {
	private float minPrice = 0;
	private float maxPrice = Integer.MAX_VALUE;//2^31
	private int pageNo;
	
	
	public CriteriaBook(float minPrice, float maxPrice, int pageNo) {
		super();
		this.minPrice = minPrice;
		this.maxPrice = maxPrice;
		this.pageNo = pageNo;
	}
	public float getMinPrice() {
		return minPrice;
	}
	public void setMinPrice(float minPrice) {
		this.minPrice = minPrice;
	}
	public float getMaxPrice() {
		return maxPrice;
	}
	public void setMaxPrice(float maxPrice) {
		this.maxPrice = maxPrice;
	}
	public int getPageNo() {
		return pageNo;
	}
	public void setPageNo(int pageNo) {
		this.pageNo = pageNo;
	}
	@Override
	public String toString() {
		return "CriteriaBook [minPrice=" + minPrice + ", maxPrice=" + maxPrice
				+ ", pageNo=" + pageNo + "]";
	}
	
}
