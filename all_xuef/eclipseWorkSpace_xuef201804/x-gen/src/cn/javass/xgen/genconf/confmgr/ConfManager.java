package cn.javass.xgen.genconf.confmgr;

import java.util.HashMap;
import java.util.Map;

import cn.javass.xgen.genconf.vo.GenConfModel;
import cn.javass.xgen.genconf.vo.ModuleConfModel;

/**
 * ���������ȡ�������ݣ���������������
 * @author moveb
 */
public class ConfManager {
	// ʵ��Ϊ����
	private static ConfManager confmgr = new ConfManager();
	private ConfManager(){
		readConf();
	}
	
	public static ConfManager getInstance(){
		return confmgr;
	}
	
	// ������������
	private GenConfModel genConfModel = new GenConfModel();
	public Map<String, ModuleConfModel> mapModuleConf = 
			new HashMap<String, ModuleConfModel>(); 
	
	public GenConfModel getGenConfModel() {
		return genConfModel;
	}

	private void setGenConfModel(GenConfModel genConfModel) {
		this.genConfModel = genConfModel;
	}

	public Map<String, ModuleConfModel> getMapModuleConf() {
		return mapModuleConf;
	}

	private void setMapModuleConf(Map<String, ModuleConfModel> mapModuleConf) {
		this.mapModuleConf = mapModuleConf;
	}

	private void readConf() {
		// ��ȡ�����ļ����������Ӧ��model
		
	}
}