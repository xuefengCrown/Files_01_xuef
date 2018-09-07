import helper.ParseImgName;
import map_imgs.QuadTree;
import map_imgs.Tile;

import java.util.*;

/**
 * This class provides all code necessary to take a query box and produce
 * a query result. The getMapRaster method must return a Map containing all
 * seven of the required fields, otherwise the front end code will probably
 * not draw the output correctly.
 */
public class Rasterer {
    // xuef add
    private QuadTree qt;
    // at our longitude (38 degrees north), each degree of longitude is SL = 288200 feet.
    private static double SL = 288200.0;
    private static double[] lonDPPs = {0, 0.78125, 1.5625, 3.125, 6.25, 12.5, 25.0, 49.0}; // d7~d1
    public Rasterer() {
        // YOUR CODE HERE
        qt = new QuadTree();
        //System.out.println(qt.getRoot().getSe().getSe().getSe().getSe().getSe().getName());
        //iter(qt.getRoot());
    }
    public static void iter(Tile tile){
        //System.out.println(tile.getName() + " ----- " + tile.getUllon() + "::" + tile.getLrlon());
        if(tile.getDepth() == 4){
            return;
        }
        iter(tile.getNw());
        iter(tile.getNe());
        iter(tile.getSw());
        iter(tile.getSe());
    }
    /**
     * Takes a user query and finds the grid of images that best matches the query. These
     * images will be combined into one big image (rastered) by the front end. <br>
     *
     *     The grid of images must obey the following properties, where image in the
     *     grid is referred to as a "tile".
     *     <ul>
     *         <li>The tiles collected must cover the most longitudinal distance per pixel
     *         (LonDPP) possible, while still covering less than or equal to the amount of
     *         longitudinal distance per pixel in the query box for the user viewport size. </li>
     *         <li>Contains all tiles that intersect the query bounding box that fulfill the
     *         above condition.</li>
     *         <li>The tiles must be arranged in-order to reconstruct the full image.</li>
     *     </ul>
     *
     * @param params Map of the HTTP GET request's query parameters - the query box and
     *               the user viewport width and height.
     *
     * @return A map of results for the front end as specified: <br>
     * "render_grid"   : String[][], the files to display. <br>
     * "raster_ul_lon" : Number, the bounding upper left longitude of the rastered image. <br>
     * "raster_ul_lat" : Number, the bounding upper left latitude of the rastered image. <br>
     * "raster_lr_lon" : Number, the bounding lower right longitude of the rastered image. <br>
     * "raster_lr_lat" : Number, the bounding lower right latitude of the rastered image. <br>
     * "depth"         : Number, the depth of the nodes of the rastered image <br>
     * "query_success" : Boolean, whether the query was able to successfully complete; don't
     *                    forget to set this to true on success! <br>
     */
    public Map<String, Object> getMapRaster(Map<String, Double> params) {
        System.out.println(params);
        Map<String, Object> results = new HashMap<>();
        //System.out.println("Since you haven't implemented getMapRaster, nothing is displayed in "
        //                   + "your browser.");
        // 根据分辨率来确定所需图片层次
        /**
         * {lrlon=-122.21835720062256, ullon=-122.27625, w=1349.0, h=662.0,
         * ullat=37.88, lrlat=37.85756921812475}
         */
        // 1. 计算 LonDPP--Longitude Distance Per Pixel
        double ullon = params.get("ullon");
        double lrlon = params.get("lrlon");
        double ullat = params.get("ullat");
        double lrlat = params.get("lrlat");
        double w = params.get("w");

        double xDist = Math.abs(lrlon-ullon);
        double lonDPP = xDist/w * SL;
        //System.out.println("lonDPP*****" + lonDPP);
        int depth = 0; // 所需图片的深度(0-7)
        for(int i=0; i<lonDPPs.length; i++){
            if(lonDPPs[i] >= lonDPP){
                depth = lonDPPs.length - i;
                break;
            }
        }

        //System.out.println("depth*****" + depth);
        // 2. 确定需要哪些图片块
        Tile ultile = locateTile(ullon, ullat, qt.getRoot(), depth);
        Tile lrtile = locateTile(lrlon, lrlat, qt.getRoot(), depth);
        String ulTileName = ultile.getName();
        String lrTileName = lrtile.getName();
        //System.out.println(ulTileName + "-----" + lrTileName);
        int lowX = Integer.parseInt(ParseImgName.sufixOfX(ulTileName));
        int lowY = Integer.parseInt(ParseImgName.sufixOfY(ulTileName));
        int upX = Integer.parseInt(ParseImgName.sufixOfX(lrTileName));
        int upY = Integer.parseInt(ParseImgName.sufixOfY(lrTileName));
        //System.out.println(lowX + "--" + upX + "**" + lowY + "--" + upY);
        String[][] render_grid = new String[upY-lowY+1][upX-lowX+1];

        List<String> l = new ArrayList<>();
        for(int j = lowY; j <= upY; j++){
            for(int k = lowX; k <= upX; k++){
                l.add(ParseImgName.consImgName(depth+"", k+"", j+"") + ".png");
            }
            String[] arr = new String[l.size()];
            render_grid[j-lowY] = l.toArray(arr);
            //System.out.println("render_grid: " + l);
            l.clear();
        }

        results.put("depth", depth);
        results.put("query_success", true);
        results.put("render_grid", render_grid);
        // 位图的上下界
        results.put("raster_ul_lon", ultile.getUllon());
        results.put("raster_lr_lon", lrtile.getLrlon());
        results.put("raster_ul_lat", ultile.getUllat());
        results.put("raster_lr_lat", lrtile.getLrlat());
        return results;
    }

    /**
     * 在目标深度的图片中定位 (lon, lat)
     * @param lon
     * @param lat
     * @param tile
     * @param depth
     * @return
     */
    public static Tile locateTile(double lon, double lat, Tile tile, int depth){
        if(tile.getDepth() == depth && isIn(lon, lat, tile)){
            return tile;
        }
        Tile[] tiles = {tile.getNw(), tile.getNe(), tile.getSw(), tile.getSe()};
        for (Tile t:tiles){
            if(isIn(lon, lat, t)){
                return locateTile(lon, lat, t, depth);
            }
        }
        return null;
    }
    /**
     * is point(lon, lat) in tile?
     * @param lon
     * @param lat
     * @param tile
     */
    public static boolean isIn(double lon, double lat, Tile tile){
        if(tile.getUllon() < lon && lon <= tile.getLrlon()
                && tile.getUllat() >= lat && lat > tile.getLrlat()){
            return true;
        }
        return false;
    }
}
