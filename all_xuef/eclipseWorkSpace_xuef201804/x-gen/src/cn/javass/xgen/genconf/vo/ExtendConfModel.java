package cn.javass.xgen.genconf.vo;

public class ExtendConfModel {
	private String extendId;
	private String value;
	private String[] values;
	private boolean isSingle = true;
	public String getExtendId() {
		return extendId;
	}
	public void setExtendId(String extendId) {
		this.extendId = extendId;
	}
	public String getValue() {
		return value;
	}
	public void setValue(String value) {
		this.value = value;
	}
	public String[] getValues() {
		return values;
	}
	public void setValues(String[] values) {
		this.values = values;
	}
	public boolean isSingle() {
		return isSingle;
	}
	public void setSingle(boolean isSingle) {
		this.isSingle = isSingle;
	}
	
	
}
