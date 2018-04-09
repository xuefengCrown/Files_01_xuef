package cn.javass.xgen.genconf.vo;

import java.util.HashMap;
import java.util.Map;

public class GenTypeModel {
	private String id;
	private String genTypeClass;
	private Map<String, String> mapParams = new HashMap<String, String>();
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getGenTypeClass() {
		return genTypeClass;
	}
	public void setGenTypeClass(String genTypeClass) {
		this.genTypeClass = genTypeClass;
	}
	public Map<String, String> getMapParams() {
		return mapParams;
	}
	public void setMapParams(Map<String, String> mapParams) {
		this.mapParams = mapParams;
	}
}
