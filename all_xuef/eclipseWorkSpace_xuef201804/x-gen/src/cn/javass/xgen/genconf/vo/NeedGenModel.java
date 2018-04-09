package cn.javass.xgen.genconf.vo;

import java.util.HashMap;
import java.util.Map;

public class NeedGenModel {
	private String id;
	private String provider;
	private String theme;
	
	private Map<String, String> mapParams = new HashMap<String, String>();

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getProvider() {
		return provider;
	}

	public void setProvider(String provider) {
		this.provider = provider;
	}

	public String getTheme() {
		return theme;
	}

	public void setTheme(String theme) {
		this.theme = theme;
	}

	public Map<String, String> getMapParams() {
		return mapParams;
	}

	public void setMapParams(Map<String, String> mapParams) {
		this.mapParams = mapParams;
	}
	
}
