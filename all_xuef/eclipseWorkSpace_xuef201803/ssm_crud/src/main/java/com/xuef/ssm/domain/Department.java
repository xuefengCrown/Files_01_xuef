package com.xuef.ssm.domain;

public class Department {
    private Integer dNo;

    private String dName;

    private String dLocation;

    public Integer getdNo() {
        return dNo;
    }

    public void setdNo(Integer dNo) {
        this.dNo = dNo;
    }

    public String getdName() {
        return dName;
    }

    public void setdName(String dName) {
        this.dName = dName == null ? null : dName.trim();
    }

    public String getdLocation() {
        return dLocation;
    }

    public void setdLocation(String dLocation) {
        this.dLocation = dLocation == null ? null : dLocation.trim();
    }

	@Override
	public String toString() {
		return "Department [dNo=" + dNo + ", dName=" + dName + ", dLocation="
				+ dLocation + "]";
	}
}