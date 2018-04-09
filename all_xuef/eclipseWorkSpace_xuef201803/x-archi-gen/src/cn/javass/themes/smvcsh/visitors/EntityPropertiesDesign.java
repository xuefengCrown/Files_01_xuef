


// Source File Name:   EntityPropertiesDesign.java

package cn.javass.themes.smvcsh.visitors;

import cn.javass.xgen.genconf.vo.ExtendConfModel;
import cn.javass.xgen.genconf.vo.ModuleConfModel;
import cn.javass.xgen.template.visitors.TemplateElement;
import cn.javass.xgen.template.visitors.Visitor;
import java.util.Map;

public class EntityPropertiesDesign
    implements Visitor
{

    public EntityPropertiesDesign()
    {
    }

    public Object visitTemplateElement(TemplateElement element)
    {
        ModuleConfModel moduleConf = element.getModuleConf();
        return genProperties(moduleConf, "voFields", "voFieldsTypes");
    }

    private static String genProperties(ModuleConfModel moduleConf, String fieldsName, String fieldsTypesName)
    {
        String voFields[] = ((ExtendConfModel)moduleConf.getMapExtends().get(fieldsName)).getValues();
        String voFieldsTypes[] = ((ExtendConfModel)moduleConf.getMapExtends().get(fieldsTypesName)).getValues();
        StringBuffer buffer = new StringBuffer("");
        for(int i = 0; i < voFields.length; i++)
            buffer.append((new StringBuilder("private ")).append(voFieldsTypes[i]).append(" ").append(voFields[i]).append(";\n\t").toString());

        return buffer.toString();
    }
}
