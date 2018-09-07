package helper;

/**
 * Created by moveb on 2018/8/30.
 * 解析图片名 d1_x0_y0
 */
public class ParseImgName {
    public static String sufixOfX(String imgName){
        String[] strs = imgName.split("_");
        String xs = strs[1];
        return xs.substring(1, xs.length());
    }
    public static String sufixOfY(String imgName){
        String[] strs = imgName.split("_");
        String xs = strs[2];
        return xs.substring(1, xs.length());
    }

    public static String consImgName(String sufixD, String sufixX, String sufixY){
        return "d" + sufixD + "_" + "x" + sufixX + "_" + "y" + sufixY;
    }
    public static void main(String[] args){
        String rs = sufixOfX("d1_x0_y1");
        String rsy = sufixOfY("d1_x0_y1");
        System.out.println(rs);
        System.out.println(rsy);
    }
}
