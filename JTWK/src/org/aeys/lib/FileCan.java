package org.aeys.lib;

import java.io.*;

import org.aeys.tools.systool;

public class FileCan {

	public static void main(String[] args) throws Exception {
		reset();
        fwrite("123\n4518\nasdgd\ndfn", "d:/test.html");
        String result = fread("d:/test.html");
        System.out.println(result);
    }
	public static void reset(){
		System.out.print("this is writeFile class");
	}

    /**
     * 鍐欏叆鏂囦欢
     * @param content 鍐呭
     * @param filename 鏂囦欢鍚嶈矾寰�
     * @return
     * @throws Exception
     */
	public static boolean fwrite(final String content,final String filename)throws Exception{
		File fname = new File(filename);
        RandomAccessFile mm = null;
        boolean flag = false;
        try{
            FileOutputStream o = new FileOutputStream(fname);
            o.write(content.getBytes("GBK"));
            o.close();
            flag = true;
        }catch (Exception e){
            e.printStackTrace();
        }finally {
            if (mm!=null){
                mm.close();
            }
        }
        return flag;
    }

    /**
     * 鏂囨湰鍐欏叆琛�
     * @param line
     * @param filename
     * @throws IOException
     */
    public static void fwline(final String line,final String filename){
        System.out.println(systool.getformat("鏂囦欢锛�%s", filename));
        try {
            FileWriter fw = new FileWriter(filename,true);
            fw.write(line);
            fw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * 璇诲彇鏂囦欢
     * @note 璁颁綇杩欓噷浣跨敤\r\n杩涜鍒嗚锛屽悗闈㈢殑绋嬪簭閮藉緱涓ユ牸鎸夌収姝ゆ柟娉曞垎琛岋紝鍚﹀垯灏嗕細瀵艰嚧绋嬪簭杩愯澶辫触
     * @param path
     * @return
     */
    public static String fread(String path){
        String data;
        String result = "";
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(path)));
            while ((data = br.readLine())!=null)
            {
                if(data.length()>1){
                    result = result + data + "\r\n";
                }
            }
            br.close();
        }catch (Exception e){
            e.printStackTrace();
        }
        return  result;
    }

    /**
     * 鍒犻櫎鏂囦欢
     */
    public static void deleteFile(String path){
        File f = new File(path);
        if(f.exists()) f.delete();
    }
}
