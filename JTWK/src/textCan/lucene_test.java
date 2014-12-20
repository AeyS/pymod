package textCan;

import org.aeys.keyword.nearSort.AvgSort;
import org.aeys.lib.FileCan;
import org.aeys.keyword.nearSort.keylayer;
import org.aeys.lib.iniFrw;
import org.aeys.tools.ArrayCan;

import java.io.File;

public class lucene_test {

    public void sort(){
        String res = FileCan.fread("D:/names.txt");
        String[] sr = res.split("\\r\\n");
        AvgSort avg = new AvgSort();
        ArrayCan arc = new ArrayCan();
//        avg.sortcolumn(sr);
        arc.prls(avg.sortcolumn(sr).split("\\r\\n"));
    }

    public String[] loadXXword(){
        iniFrw ini = new iniFrw();
        ini.link("./loadXXword.ini");
        String[] XXword = ini.KeyValueRead("XXword","word").split("\\|");
        return XXword;
    }

    public void run_IKA(){
        File fp = new File("src/temp");
        if (!fp.exists() && !fp.isDirectory()){fp.mkdirs();}
        fp = null;
        String res = FileCan.fread("D:/names.txt");
        String[] sr = res.split("\\r\\n");
        ArrayCan arc = new ArrayCan();
        String[] result = arc.trans_StrArr(arc.lsord(arc.trans_ListArr(sr)));
        String[] EntryJsonArr = keylayer.IKAsisArrayToJson(result);
        String[] word = loadXXword();
        keylayer.Analysis(EntryJsonArr,word,true);
        System.exit(0);
    }
	
	public static void main(String[] args){
        lucene_test lc = new lucene_test();
        lc.run_IKA();
    }
}