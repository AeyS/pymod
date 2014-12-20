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
 * ~Classfunction �ؼ���
 * ~Explain ���Ϸִ���ϵ,�ִ���ȫ����IKAnalyzer2012
 * ~Note �������ϵĽ��������ɴ���json
 * =====================================
 */
public class keylayer{
    /**
     * �ִʹ���
     * @param str
     * @return
     */
    public static String IKAsis(String str){
        KeyToEntry kte = new KeyToEntry();
        return kte.SplitEntry(str);
    }

    /**
     * �ִʹ������json�ֶ�
     * @param str
     * @return json
     */
    public static String IKAsisToJson(String str){
        KeyToEntry kte = new KeyToEntry();
        return kte.tojson(kte.SplitEntry(str));
    }

    /**
     * �ִʹ���--�ʻ�������json�ֶ�
     * @param Arrstr �ַ�������
     * @return Entrypool
     */
    public static String[] IKAsisArrayToJson(String[] Arrstr){
        KeyToEntry kte = new KeyToEntry();
        return kte.Arraytojson(Arrstr);
    }

    /**
     * �ַ��ʻ�
     * @param EntryJsonArr
     * @param flag
     */
    public static void Analysis(String[] EntryJsonArr,String[] word,boolean flag){
        Analysis ays = new Analysis();
        ArrayCan arc = new ArrayCan();
        warehouse wh = new warehouse();
        File f = new File(wh.fomatpath(wh.ssdininpath));
        if (flag && f.exists()) {
            wh.deleteSSD();// ��չ�̬�ֿ�
            wh.cleanSsdpath();// ��չ�̬�ֿ�·����¼
        }

        Entry ety = (Entry) JSON.parse(EntryJsonArr[0]);
        String[] topkey = arc.trans_StrArr(ety.getEntryArr());
        String[] key;// ��ϴ�

        List arr = arc.trans_ListArr(word);

        for (int i = 0; i < topkey.length; i+=2) {
        	Object[] printObj = new Object[1];
        	printObj[0] = Integer.valueOf(i); printObj[1] = Integer.valueOf(topkey.length);
            System.out.println(String.format("��ǰ����%d,��ǰ�ܳ�%d", printObj));
            if (topkey.length<2){
                System.out.println(topkey[0]);
                // ����ؼ���С��2������Ҫ�ַ�����������Ϊֻ��һ���Ĺؼ����޷�����
                List EntryJsonArrNew = arc.removeIndex(0,EntryJsonArr);
                EntryJsonArr = arc.trans_StrArr(EntryJsonArrNew);
                break;
            }else if (i==topkey.length-1) break;//������� i ����topkey.lenght-1  ����ô����һ��������ֻ�е�һ�ʻ㣬�������жϣ�����
            key = new String[]{topkey[i], topkey[i+1]};
            System.out.println("--����ʣ�"+key[0]+key[1]);

            //���˽��ôʻ�
            for (; i < word.length; i++) {
                if (arr.contains(key)) {
                    System.out.println("�����Ϊ���ôʻ㣺"+key[0]+key[1]);
                    break;
                }
            }
            List EntryResult = ays.token(EntryJsonArr,key);
            // ���طַ����ʣ����
            EntryJsonArr = arc.trans_StrArr(EntryResult);
        }

        // ������С��1��ʱ�򣬳���ֹͣ
        if (EntryJsonArr.length>0){
            System.out.println("---------����һ������---------");
            Analysis(EntryJsonArr,word,false);
        }
    }
}


/**
 * -------------------------
 * �ؼ���ת����json�ṹ���ϴ���
 * -------------------------
 */
class KeyToEntry {
    private long id;
    /**
     * �ָ����
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
     * ������תΪjson,��classname
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
     * ������תΪjson
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
 * json��������,���ҷַ����ڴ�ֿ�
 * ------------------------------
 */
class Analysis{
    /**
     * �ַ������ڵ����й���keyword�Ĵ�������ʱ�ֿ�
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
        // ����ؼ���ƥ��õ���������ô����������ʱ�ֿ�ת�Ƶ���̬�ֿ�
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
     * ��������
     * @param entryJsonArr
     */
    public void analysisEntry(String[] entryJsonArr){

    }
}


/**
 * �ڴ�ֿ�����
 * @author XIN
 *
 */
class warehouse{
    private final String temppath = "temppath";
    protected final String ssdininpath = "ssdininpath";
    private String ssdpath;
    public List temp;

    /**
     * ��ʽ��·����ʽ
     * @param fomat
     * @param path
     * @return
     */
    public String fomatpath(String path){
    	return systool.getformat("src/temp/%s.log", path);
    }
    /**
     * д����ʱ�ֿ�
     * @param entry
     */
    public void tempSave(String entry){
    	Object[] printObj = new Object[1];
    	printObj[0] = fomatpath(temppath);
        System.out.println(String.format("������ʱ�ֿ�%s", printObj));
    	printObj[0] = entry;
        FileCan.fwline(String.format("%s\r\n", printObj), fomatpath(temppath));
    }

    /**
     * ��ȡ��ʱ�ֿ�
     */
    public String[] tempLoad(){
    	System.out.println(systool.getformat("������ʱ�ֿ�%s", fomatpath(temppath)));
        System.out.println(systool.getformat("������ʱ�ֿ�%s",fomatpath(temppath)));
        return FileCan.fread(systool.getformat("src/temp/%s.log",temppath)).split("\\r\\n");
    }

    /**
     * �����ʱ�ֿ��ڵ���Ϣ
     */
    public void cleantemp(){
        System.out.println(systool.getformat("�����ʱ�ֿ�%s",fomatpath(temppath)));
        try {
            FileCan.fwrite("", fomatpath(temppath));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * ɾ��temp�ļ�
     */
    public void deletetemp(){
        System.out.println(systool.getformat("ɾ����ʱ�ֿ�%s",fomatpath(temppath)));
        FileCan.deleteFile(fomatpath(temppath));
    }

    /**
     * ��¼path·��
     * @param path
     */
    public void setSsdpath(String path){
        System.out.println(systool.getformat("���ü���¼��̬�ֿ�·��%s",fomatpath(ssdininpath)));
        this.ssdpath = path;
        String[] inipath = FileCan.fread(fomatpath(ssdininpath)).split("\\r\\n");
        ArrayCan arc = new ArrayCan();
        if (!arc.existIn(inipath,ssdpath))
            FileCan.fwline(systool.getformat("%s\r\n", path), fomatpath(ssdininpath));
    }

    /**
     * ��ȡpath·��
     */
    public String[] getSsdpath(){
        System.out.println(systool.getformat("�����̬�ֿ�·��%s",fomatpath(ssdininpath)));
        return FileCan.fread(fomatpath(ssdininpath)).split("\\r\\n");
    }

    /**
     * ��չ�̬�ֿ�·����¼
     */
    public void cleanSsdpath(){
        System.out.println(systool.getformat("��չ�̬�ֿ�·����¼%s",fomatpath(ssdininpath)));
        try {
            FileCan.fwrite("",fomatpath(ssdininpath));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * д���̬�ֿ�
     * ���ϼ����ó����趨ssdpath
     * @param entryArr
     */
    public void SSDsave(String[] entryArr){
        //���ֻ��һ���Ĵ�����ֱ�ӷ���AllonlyOne,�������п��ٹ�̬�ֿ�
        if (entryArr.length<2){
            setSsdpath("AllonlyOne");
        }else{
            // ���3��һ��ϲ��ؼ���
            AvgSort avg = new AvgSort();
            entryArr = avg.sortcolumn(entryArr).split("\\r\\n");
        }
        System.out.println(systool.getformat("�����̬�ֿ�%s",systool.getformat("src/temp/SSDto%s.log",ssdpath)));
        for (int i = 0; i < entryArr.length; i++) {
            FileCan.fwline(systool.getformat("%s\r\n", entryArr[i]), systool.getformat("src/temp/SSDto%s.log", ssdpath));
        }
    }

    /**
     * ��ȡ��̬�ֿ�
     * ���ϼ����ó����趨ssdpath
     */
    public String[] SSDload(){
        System.out.println(systool.getformat("�����̬�ֿ�%s",systool.getformat("src/temp/SSDto%s.log",ssdpath)));
        return FileCan.fread(systool.getformat("src/temp/SSDto%s.log",ssdpath)).split("\\r\\n");
    }

    /**
     * ���������̬�ֿ�
     * ������й�̬�ֿ��ڵ���Ϣ
     */
    public void cleanOnlyOneSSD(){
        try {
            System.out.println(systool.getformat("��չ�̬�ֿ�%s",systool.getformat("src/temp/SSDto%s.log",ssdpath)));
            FileCan.fwrite("", systool.getformat("src/temp/SSDto%s.log",ssdpath));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * ������й�̬�ֿ��ڵ���Ϣ
     */
    public void cleanAllSSD(){
        String[] path = getSsdpath();
        for (int i = 0; i <path.length; i++) {
            try {
                System.out.println(systool.getformat("��չ�̬�ֿ�%s",systool.getformat("src/temp/SSDto%s.log",path[i])));
                FileCan.fwrite("", systool.getformat("src/temp/SSDto%s.log",path[i]));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * ɾ�����й�̬�ֿ��ڵ���Ϣ
     */
    public void deleteSSD(){
        String[] path = getSsdpath();
        for (int i = 0; i <path.length; i++) {
            System.out.println(systool.getformat("ɾ����̬�ֿ�%s",systool.getformat("src/temp/SSDto%s.log",path[i])));
            FileCan.deleteFile(systool.getformat("src/temp/SSDto%s.log",path[i]));
        }
    }
}