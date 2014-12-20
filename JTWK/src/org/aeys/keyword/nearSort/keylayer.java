package org.aeys.keyword.nearSort;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;

import org.aeys.lib.FileCan;
import org.aeys.tools.ArrayCan;
import org.aeys.tools.systool;
import org.wltea.analyzer.core.IKSegmenter;
import org.wltea.analyzer.core.Lexeme;

import java.io.*;
import java.util.ArrayList;
import java.util.List;


/**
 * =====================================
 * ~Classfunction 关键层
 * ~Explain 语料分词体系,分词完全依赖IKAnalyzer2012
 * ~Note 负责语料的解析，生成词条json
 * =====================================
 */
public class keylayer{
    /**
     * 分词工具
     * @param str
     * @return
     */
    public static String IKAsis(String str){
        KeyToEntry kte = new KeyToEntry();
        return kte.SplitEntry(str);
    }

    /**
     * 分词工具输出json字段
     * @param str
     * @return json
     */
    public static String IKAsisToJson(String str){
        KeyToEntry kte = new KeyToEntry();
        return kte.tojson(kte.SplitEntry(str));
    }

    /**
     * 分词工具--词汇队列输出json字段
     * @param Arrstr 字符串数组
     * @return Entrypool
     */
    public static String[] IKAsisArrayToJson(String[] Arrstr){
        KeyToEntry kte = new KeyToEntry();
        return kte.Arraytojson(Arrstr);
    }

    /**
     * 分发词汇
     * @param EntryJsonArr
     * @param flag
     */
    public static void Analysis(String[] EntryJsonArr,String[] word,boolean flag){
        Analysis ays = new Analysis();
        ArrayCan arc = new ArrayCan();
        warehouse wh = new warehouse();
        File f = new File(wh.fomatpath(wh.ssdininpath));
        if (flag && f.exists()) {
            wh.deleteSSD();// 清空固态仓库
            wh.cleanSsdpath();// 清空固态仓库路径记录
        }

        Entry ety = (Entry) JSON.parse(EntryJsonArr[0]);
        String[] topkey = arc.trans_StrArr(ety.getEntryArr());
        String[] key;// 组合词

        List arr = arc.trans_ListArr(word);

        for (int i = 0; i < topkey.length; i+=2) {
        	Object[] printObj = new Object[1];
        	printObj[0] = Integer.valueOf(i); printObj[1] = Integer.valueOf(topkey.length);
            System.out.println(String.format("当前迭代%d,当前总长%d", printObj));
            if (topkey.length<2){
                System.out.println(topkey[0]);
                // 如果关键词小于2个则不需要分发，跳过，因为只有一个的关键词无法归类
                List EntryJsonArrNew = arc.removeIndex(0,EntryJsonArr);
                EntryJsonArr = arc.trans_StrArr(EntryJsonArrNew);
                break;
            }else if (i==topkey.length-1) break;//如果迭代 i 等于topkey.lenght-1  ，那么这是一个奇数，只有单一词汇，做不了判断，跳过
            key = new String[]{topkey[i], topkey[i+1]};
            System.out.println("--归类词："+key[0]+key[1]);

            //过滤禁用词汇
            for (; i < word.length; i++) {
                if (arr.contains(key)) {
                    System.out.println("归类词为禁用词汇："+key[0]+key[1]);
                    break;
                }
            }
            List EntryResult = ays.token(EntryJsonArr,key);
            // 返回分发后的剩余结果
            EntryJsonArr = arc.trans_StrArr(EntryResult);
        }

        // 当数组小于1的时候，程序停止
        if (EntryJsonArr.length>0){
            System.out.println("---------换下一个词条---------");
            Analysis(EntryJsonArr,word,false);
        }
    }
}


/**
 * -------------------------
 * 关键词转换成json结构语料词条
 * -------------------------
 */
class KeyToEntry {
    private long id;
    /**
     * 分割词条
     * @param str
     * @return
     */
    public String SplitEntry(String str){
        StringBuffer sb = new StringBuffer();
        try{
            byte[] bt = str.getBytes();
            InputStream ip = new ByteArrayInputStream(bt);
            Reader read = new InputStreamReader(ip);
            IKSegmenter iks = new IKSegmenter(read, true);
            Lexeme t;
            while ((t = iks.next())!=null){
                sb.append(t.getLexemeText()+"|");
            }
            sb.delete(sb.length()-1, sb.length());
        }catch(IOException e){
            e.printStackTrace();
        }
//        System.out.println(sb.toString());
        return sb.toString();
    }
    /**
     * 将词条转为json,带classname
     * @return
     */
    public String tojson(String entry){
        Entry ety = new Entry();
        ArrayCan arc = new ArrayCan();
        ety.setId(id+1);
        id+=1;
        ety.setEntry(entry.replace("|", ""));
        ety.setEntryArr(arc.trans_ListArr(entry.split("\\|")));
        SerializerFeature[] feature = {SerializerFeature.WriteClassName};
        String json = JSON.toJSONString(ety, feature);
//        System.out.println(json);
        return json;
    }

    /**
     * 将词条转为json
     * @return
     */
    public String[] Arraytojson(String[] Arrstr){
        KeyToEntry kte = new KeyToEntry();
        String[] Entrypool = new String[Arrstr.length];
        for (int i=0; i<Arrstr.length; i++){
            Entrypool[i] = kte.tojson(kte.SplitEntry(Arrstr[i]));
        }
        return Entrypool;
    }
}


/**
 * ------------------------------
 * json词条分析,并且分发给内存仓库
 * ------------------------------
 */
class Analysis{
    /**
     * 分发队列内的所有关于keyword的词条到临时仓库
     * @param EntryJsonArr
     * @param keyword
     */
    public List token(String[] EntryJsonArr,String[] keyword){
        ArrayCan arc = new ArrayCan();
        warehouse wh = new warehouse();
        boolean flag = false;
        int arrayLength = 0;
        List EntryResult = new ArrayList();
        for (int i = 0; i < EntryJsonArr.length; i++) {
            Entry ety = (Entry) JSON.parse(EntryJsonArr[i]);
            if (arc.existIn(arc.trans_StrArr(ety.getEntryArr()),keyword[0]) &&
                    arc.existIn(arc.trans_StrArr(ety.getEntryArr()),keyword[1])){
                flag = true;
                arrayLength+=1;
                System.out.println(ety.getEntryArr());
                wh.tempSave(ety.getEntry());
            }else{
                EntryResult.add(EntryJsonArr[i]);
            }
        }
        // 如果关键词匹配得到词条，那么将词条从临时仓库转移到固态仓库
        if (flag) {
            if (arrayLength>1){
                wh.setSsdpath(keyword[0]+keyword[1]);
            }
            wh.SSDsave(wh.tempLoad());
            wh.cleantemp();
        }
        keyword = null;
        return EntryResult;
    }

    /**
     * 分析词条
     * @param entryJsonArr
     */
    public void analysisEntry(String[] entryJsonArr){

    }
}


/**
 * 内存仓库容器
 * @author XIN
 *
 */
class warehouse{
    private final String temppath = "temppath";
    protected final String ssdininpath = "ssdininpath";
    private String ssdpath;
    public List temp;

    /**
     * 格式化路径格式
     * @param fomat
     * @param path
     * @return
     */
    public String fomatpath(String path){
    	return systool.getformat("src/temp/%s.log", path);
    }
    /**
     * 写入临时仓库
     * @param entry
     */
    public void tempSave(String entry){
    	Object[] printObj = new Object[1];
    	printObj[0] = fomatpath(temppath);
        System.out.println(String.format("存入临时仓库%s", printObj));
    	printObj[0] = entry;
        FileCan.fwline(String.format("%s\r\n", printObj), fomatpath(temppath));
    }

    /**
     * 读取临时仓库
     */
    public String[] tempLoad(){
    	System.out.println(systool.getformat("载入临时仓库%s", fomatpath(temppath)));
        System.out.println(systool.getformat("载入临时仓库%s",fomatpath(temppath)));
        return FileCan.fread(systool.getformat("src/temp/%s.log",temppath)).split("\\r\\n");
    }

    /**
     * 清空临时仓库内的信息
     */
    public void cleantemp(){
        System.out.println(systool.getformat("清空临时仓库%s",fomatpath(temppath)));
        try {
            FileCan.fwrite("", fomatpath(temppath));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * 删除temp文件
     */
    public void deletetemp(){
        System.out.println(systool.getformat("删除临时仓库%s",fomatpath(temppath)));
        FileCan.deleteFile(fomatpath(temppath));
    }

    /**
     * 记录path路径
     * @param path
     */
    public void setSsdpath(String path){
        System.out.println(systool.getformat("设置及记录固态仓库路径%s",fomatpath(ssdininpath)));
        this.ssdpath = path;
        String[] inipath = FileCan.fread(fomatpath(ssdininpath)).split("\\r\\n");
        ArrayCan arc = new ArrayCan();
        if (!arc.existIn(inipath,ssdpath))
            FileCan.fwline(systool.getformat("%s\r\n", path), fomatpath(ssdininpath));
    }

    /**
     * 获取path路径
     */
    public String[] getSsdpath(){
        System.out.println(systool.getformat("载入固态仓库路径%s",fomatpath(ssdininpath)));
        return FileCan.fread(fomatpath(ssdininpath)).split("\\r\\n");
    }

    /**
     * 清空固态仓库路径记录
     */
    public void cleanSsdpath(){
        System.out.println(systool.getformat("清空固态仓库路径记录%s",fomatpath(ssdininpath)));
        try {
            FileCan.fwrite("",fomatpath(ssdininpath));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * 写入固态仓库
     * 由上级调用程序设定ssdpath
     * @param entryArr
     */
    public void SSDsave(String[] entryArr){
        //如果只有一个的词条，直接放入AllonlyOne,不再另行开辟固态仓库
        if (entryArr.length<2){
            setSsdpath("AllonlyOne");
        }else{
            // 最大3个一组合并关键词
            AvgSort avg = new AvgSort();
            entryArr = avg.sortcolumn(entryArr).split("\\r\\n");
        }
        System.out.println(systool.getformat("存入固态仓库%s",systool.getformat("src/temp/SSDto%s.log",ssdpath)));
        for (int i = 0; i < entryArr.length; i++) {
            FileCan.fwline(systool.getformat("%s\r\n", entryArr[i]), systool.getformat("src/temp/SSDto%s.log", ssdpath));
        }
    }

    /**
     * 读取固态仓库
     * 由上级调用程序设定ssdpath
     */
    public String[] SSDload(){
        System.out.println(systool.getformat("载入固态仓库%s",systool.getformat("src/temp/SSDto%s.log",ssdpath)));
        return FileCan.fread(systool.getformat("src/temp/SSDto%s.log",ssdpath)).split("\\r\\n");
    }

    /**
     * 清除单个固态仓库
     * 清空所有固态仓库内的信息
     */
    public void cleanOnlyOneSSD(){
        try {
            System.out.println(systool.getformat("清空固态仓库%s",systool.getformat("src/temp/SSDto%s.log",ssdpath)));
            FileCan.fwrite("", systool.getformat("src/temp/SSDto%s.log",ssdpath));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * 清空所有固态仓库内的信息
     */
    public void cleanAllSSD(){
        String[] path = getSsdpath();
        for (int i = 0; i <path.length; i++) {
            try {
                System.out.println(systool.getformat("清空固态仓库%s",systool.getformat("src/temp/SSDto%s.log",path[i])));
                FileCan.fwrite("", systool.getformat("src/temp/SSDto%s.log",path[i]));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * 删除所有固态仓库内的信息
     */
    public void deleteSSD(){
        String[] path = getSsdpath();
        for (int i = 0; i <path.length; i++) {
            System.out.println(systool.getformat("删除固态仓库%s",systool.getformat("src/temp/SSDto%s.log",path[i])));
            FileCan.deleteFile(systool.getformat("src/temp/SSDto%s.log",path[i]));
        }
    }
}