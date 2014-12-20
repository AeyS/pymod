package org.aeys.lib;

import org.aeys.tools.ArrayCan;

import java.io.File;
import java.util.*;

/**
 * Created by Aeys on 2014/10/25.
 */
public class text {
    public static void main(String[] args) {
		ArrayCan ac = new ArrayCan();
		String[] arrStrings = pathls("D:\\",".html",true);
		ac.prls(arrStrings);

        String[] ls = {"1","2","1","3","2"};
        List list = ac.trans_ListArr(ls);
        ac.prls(ac.trans_StrArr(ac.lsord(list)));
        
        ac.prls(ac.RandomSort(arrStrings));
    }


    
    /**
     * 閬嶅巻璺緞涓嬬殑鏂囦欢
     * @param path 鐖惰矾寰�
     * @param ABSPATH 鏄惁杩斿洖缁撳璺緞
     */
    public static String[] pathls(String path,String format,boolean ABSPATH){
        File fdir = new File(path);
        String[] flist = fdir.list();
        if (flist == null) {
			System.out.print("璺緞涓嶅瓨鍦紒");
		}
        if (ABSPATH) {
            for (int i = 0; i < flist.length; i++) {
                flist[i] = path + '\\' + flist[i];
            }
        }
        ArrayCan ac = new ArrayCan();
        String[] result = ac.FilterKeyWord(flist,format);
        return result;
    }
}