package cn.javass.xgen.genconf.vo;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
/**
 * x-gen 核心框架配置对应的数据model
 * @author moveb
 */
public class GenConfModel {
	/**
	 * 描述注册的多个用户需要生成的模块的model
	 */
	private List<NeedGenModel> needGens = new ArrayList<NeedGenModel>();
	/**
	 * 描述外部主题
	 */
	private List<ThemeModel> themes = new ArrayList<ThemeModel>();
	private Map<String, String> constants = new HashMap<String, String>();
	public List<NeedGenModel> getNeedGens() {
		return needGens;
	}
	public void setNeedGens(List<NeedGenModel> needGens) {
		this.needGens = needGens;
	}
	public List<ThemeModel> getThemes() {
		return themes;
	}
	public void setThemes(List<ThemeModel> themes) {
		this.themes = themes;
	}
	public Map<String, String> getConstants() {
		return constants;
	}
	public void setConstants(Map<String, String> constants) {
		this.constants = constants;
	}
	
}
