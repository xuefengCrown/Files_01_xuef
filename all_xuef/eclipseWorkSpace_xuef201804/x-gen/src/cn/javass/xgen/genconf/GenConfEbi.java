package cn.javass.xgen.genconf;

import java.util.Map;

import cn.javass.xgen.genconf.vo.GenConfModel;
import cn.javass.xgen.genconf.vo.ModuleConfModel;
/**
 * ����ӿ�
 * @author moveb
 */
public interface GenConfEbi {
	/**
	 * ��ȡx-gen���Ŀ������������������� model
	 * @return
	 */
	public GenConfModel getGenConf();
	/**
	 * ��ȡ��Ҫ���ɵ�����ģ�������
	 * @return ������Ҫ���ɵ�����ģ����������ݵ�Map
	 * key: ģ���id
	 * value: ��Ӧģ����������ݵ� model
	 */
	public Map<String, ModuleConfModel> getMapModuleConf();
}