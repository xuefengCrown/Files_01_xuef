package cn.javass.xgen.genconf;

import java.util.Map;

import cn.javass.xgen.genconf.confmgr.ConfManager;
import cn.javass.xgen.genconf.vo.GenConfModel;
import cn.javass.xgen.genconf.vo.ModuleConfModel;

// 负责 配置管理模块的业务功能
public class GenConfEbo implements GenConfEbi {
	// 单例的
	private static GenConfEbo genConEbo = new GenConfEbo();
	private GenConfEbo(){}
	public static GenConfEbo getInstance(){
		return genConEbo;
	}
	
	@Override
	public GenConfModel getGenConf() {
		// 实际的获取动作交给 ConfManager
		return ConfManager.getInstance().getGenConfModel();
	}

	@Override
	public Map<String, ModuleConfModel> getMapModuleConf() {
		return ConfManager.getInstance().getMapModuleConf();
	}

}
