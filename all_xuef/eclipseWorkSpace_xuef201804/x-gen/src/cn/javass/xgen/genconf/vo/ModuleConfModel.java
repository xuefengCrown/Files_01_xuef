package cn.javass.xgen.genconf.vo;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ModuleConfModel {
	// 模块标识
	private String moduleId = "";
	// 该模块使用的外部主题的标识
	private String useTheme = "";
	// 用户需要生成的具体功能，key: 功能标识 value: 功能生成后的多种输出类型的标识的集合
	private Map<String, List<String>> needGenTypes = 
			new HashMap<String, List<String>>();
	// 模块生成所需要的扩展数据， key: 数据的id  value: 对应的扩展数据的model
	private Map<String, ExtendConfModel> extds = 
			new HashMap<String, ExtendConfModel>();
	public String getModuleId() {
		return moduleId;
	}
	public void setModuleId(String moduleId) {
		this.moduleId = moduleId;
	}
	public String getUseTheme() {
		return useTheme;
	}
	public void setUseTheme(String useTheme) {
		this.useTheme = useTheme;
	}
	public Map<String, List<String>> getNeedGenTypes() {
		return needGenTypes;
	}
	public void setNeedGenTypes(Map<String, List<String>> needGenTypes) {
		this.needGenTypes = needGenTypes;
	}
	public Map<String, ExtendConfModel> getExtds() {
		return extds;
	}
	public void setExtds(Map<String, ExtendConfModel> extds) {
		this.extds = extds;
	}
}
