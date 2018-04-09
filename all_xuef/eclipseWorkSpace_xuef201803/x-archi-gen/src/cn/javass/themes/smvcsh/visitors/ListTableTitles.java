


// Source File Name:   ListTableTitles.java

package cn.javass.themes.smvcsh.visitors;

import cn.javass.xgen.genconf.vo.ExtendConfModel;
import cn.javass.xgen.genconf.vo.ModuleConfModel;
import cn.javass.xgen.template.visitors.TemplateElement;
import cn.javass.xgen.template.visitors.Visitor;
import java.util.Map;

public class ListTableTitles
    implements Visitor
{

    public ListTableTitles()
    {
    }

    public Object visitTemplateElement(TemplateElement element)
    {
        ModuleConfModel moduleConf = element.getModuleConf();
        return genProperties(moduleConf, "voFields", "voFieldsNames", "fieldNeedSorts");
    }

    private static String genProperties(ModuleConfModel moduleConf, String fieldsName, String fieldsNames, String fieldNeedSortsName)
    {
        String voFields[] = ((ExtendConfModel)moduleConf.getMapExtends().get(fieldsName)).getValues();
        String voFieldsNames[] = ((ExtendConfModel)moduleConf.getMapExtends().get(fieldsNames)).getValues();
        String fieldNeedSorts[] = ((ExtendConfModel)moduleConf.getMapExtends().get(fieldNeedSortsName)).getValues();
        StringBuffer buffer = new StringBuffer("");
        for(int i = 0; i < voFields.length; i++)
        {
            buffer.append("<th ");
            if("true".equals(fieldNeedSorts[i]))
                buffer.append((new StringBuilder("sort=\"")).append(voFields[i]).append("\"").toString());
            buffer.append((new StringBuilder(">")).append(voFieldsNames[i]).append("</th>\n\t").toString());
            buffer.append("\n\t");
        }

        return buffer.toString();
    }
}
