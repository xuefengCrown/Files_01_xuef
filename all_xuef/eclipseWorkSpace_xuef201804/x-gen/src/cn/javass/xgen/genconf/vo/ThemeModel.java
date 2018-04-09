package cn.javass.xgen.genconf.vo;

import java.util.HashMap;
import java.util.Map;

public class ThemeModel {
	private String themeId;
	private String location;
	
	private Map<String, GenTypeModel> genTypes = new HashMap<String, GenTypeModel>();
	private Map<String, String> genOutTypes = new HashMap<>();
	private Map<String, String> providers = new HashMap<>();
	public String getThemeId() {
		return themeId;
	}
	public void setThemeId(String themeId) {
		this.themeId = themeId;
	}
	public String getLocation() {
		return location;
	}
	public void setLocation(String location) {
		this.location = location;
	}
	public Map<String, GenTypeModel> getGenTypes() {
		return genTypes;
	}
	public void setGenTypes(Map<String, GenTypeModel> genTypes) {
		this.genTypes = genTypes;
	}
	public Map<String, String> getGenOutTypes() {
		return genOutTypes;
	}
	public void setGenOutTypes(Map<String, String> genOutTypes) {
		this.genOutTypes = genOutTypes;
	}
	public Map<String, String> getProviders() {
		return providers;
	}
	public void setProviders(Map<String, String> providers) {
		this.providers = providers;
	}
}
