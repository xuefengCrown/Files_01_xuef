package map_imgs;

/**
 * Created by moveb on 2018/8/30.
 * quadtree 中的 图片块节点
 */
public class Tile {
    // 图片名
    private String name;
    // 经度
    private double ullon;
    private double lrlon;
    // 纬度
    private double ullat; // upper left corner latitude
    private double lrlat; // lower right corner latitude
    // 图片所在层次
    private int depth;
    // 图片的相对位置 左上:1, 右上:2, 左下:3, 右下:4
    // 位置数据 定义为常量比较好
    private int pos;

    private Tile parent;
    private Tile nw;
    private Tile ne;
    private Tile sw;
    private Tile se;

    public double getLrlat() {
        return lrlat;
    }

    public void setLrlat(double lrlat) {
        this.lrlat = lrlat;
    }

    public double getLrlon() {
        return lrlon;
    }

    public void setLrlon(double lrlon) {
        this.lrlon = lrlon;
    }

    public double getUllat() {
        return ullat;
    }

    public void setUllat(double ullat) {
        this.ullat = ullat;
    }

    public double getUllon() {
        return ullon;
    }

    public void setUllon(double ullon) {
        this.ullon = ullon;
    }

    public int getDepth() {
        return depth;
    }

    public void setDepth(int depth) {
        this.depth = depth;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Tile getNw() {
        return nw;
    }

    public void setNw(Tile nw) {
        this.nw = nw;
    }

    public Tile getNe() {
        return ne;
    }

    public void setNe(Tile ne) {
        this.ne = ne;
    }

    public Tile getParent() {
        return parent;
    }

    public void setParent(Tile parent) {
        this.parent = parent;
    }

    public Tile getSe() {
        return se;
    }

    public void setSe(Tile se) {
        this.se = se;
    }

    public Tile getSw() {
        return sw;
    }

    public void setSw(Tile sw) {
        this.sw = sw;
    }

    public int getPos() {
        return pos;
    }

    public void setPos(int pos) {
        this.pos = pos;
    }
}

