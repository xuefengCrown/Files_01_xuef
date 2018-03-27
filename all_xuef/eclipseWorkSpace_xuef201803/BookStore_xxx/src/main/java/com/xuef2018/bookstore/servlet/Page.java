package com.xuef2018.bookstore.servlet;

import java.util.List;

public class Page<T> {
	//��ǰҳ
	private int pageNo;
	//��ǰҳ��ͼ��
	private List<T> list;
	//ÿҳ�� ��¼��
	private int pageSize = 3;
	//�ܼ�¼��
	private int totalItemNumber;
	
	// ��ȡ��ҳ��
	public int getTotalPageNumber(){
		int totalPageNumber = totalItemNumber/pageSize;
		if(totalItemNumber % pageSize !=0)
			totalPageNumber += 1;
		
		return totalPageNumber;
	}
	public boolean isHasNext(){
		if(getPageNo() < getTotalPageNumber())
			return true;
		return false;
	}
	public boolean isHasPre(){
		if(getPageNo() > 1)
			return true;
		return false;
	}
	public int getPrePage(){
		if(isHasPre()) return getPageNo()-1;
		return getPageNo();
	}
	public int getNextPage(){
		if(isHasNext()) return getPageNo() + 1;
		return getPageNo();
	}
	public Page(int pageNo) {
		super();
		this.pageNo = pageNo;
	}
	// ���˶� pageNo ��У��
	public int getPageNo() {
		if(pageNo < 0) pageNo = 1;
		if(pageNo > getTotalPageNumber()) 
			pageNo = getTotalPageNumber();
		return pageNo;
	}
	public List<T> getList() {
		return list;
	}
	public void setList(List<T> list) {
		this.list = list;
	}
	public int getPageSize() {
		return pageSize;
	}
	public void setPageSize(int pageSize) {
		this.pageSize = pageSize;
	}
	public int getTotalItemNumber() {
		return totalItemNumber;
	}
	public void setTotalItemNumber(int totalItemNumber) {
		this.totalItemNumber = totalItemNumber;
	}
	@Override
	public String toString() {
		return "Page [pageNo=" + pageNo + ", list=" + list + ", pageSize="
				+ pageSize + ", totalItemNumber=" + totalItemNumber + "]";
	}
	
}