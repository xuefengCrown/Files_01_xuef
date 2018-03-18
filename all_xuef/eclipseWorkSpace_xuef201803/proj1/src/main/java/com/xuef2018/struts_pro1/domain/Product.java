package com.xuef2018.struts_pro1.domain;

public class Product {
	private String productName;
	private String productDesc;
	private float productPrice;
	public String getProductName() {
		return productName;
	}
	public void setProductName(String productName) {
		this.productName = productName;
	}
	public String getProductDesc() {
		return productDesc;
	}
	public void setProductDesc(String productDesc) {
		this.productDesc = productDesc;
	}
	public float getProductPrice() {
		return productPrice;
	}
	public void setProductPrice(float productPrice) {
		this.productPrice = productPrice;
	}
	@Override
	public String toString() {
		return "Product [productName=" + productName + ", productDesc="
				+ productDesc + ", productPrice=" + productPrice + "]";
	}
	public String save(){
		System.out.println("save...");
		return "show";
	}
}
