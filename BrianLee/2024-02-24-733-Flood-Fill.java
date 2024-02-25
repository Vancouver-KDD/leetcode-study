https://leetcode.com/problems/flood-fill/

class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        if(newColor != image[sr][sc]) chnageColor(image, sr, sc, newColor, image[sr][sc]);
        return image;
    }

    private void chnageColor(int[][] image, int sr, int sc, int newColor, int startColor) {
        if(image[sr][sc] == startColor)
            image[sr][sc] = newColor;
        else
            return;

        if(sr+1 < image.length)    chnageColor(image, sr+1, sc, newColor, startColor);
        if(sr-1 >= 0)              chnageColor(image, sr-1, sc, newColor, startColor);
        if(sc+1 < image[0].length) chnageColor(image, sr, sc+1, newColor, startColor);
        if(sc-1 >= 0)              chnageColor(image, sr, sc-1, newColor, startColor);
    }
}