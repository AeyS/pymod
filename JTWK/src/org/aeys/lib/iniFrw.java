package org.aeys.lib;

import org.ini4j.Wini;

import java.io.File;
import java.io.IOException;

/**
 * Created by Aeys on 2014/11/23.
 */
public class iniFrw {

    private String filepath;
    private File f;

    public static void main(String[] argv)
    {
        iniFrw ifrw = new iniFrw();
        ifrw.link("d:\\long\\ini.ini");
        System.out.println(ifrw.KeyValueRead("File", "len"));
        ifrw.KeyValueWrite("File","size",123);
    }

	/**
     * �ж��ļ��Ƿ���ڣ��������򴴽�
     */
    public void link(String filepath)
    {
        this.filepath = filepath;
        this.f = new File(this.filepath);
        String path = f.getParent();
        File p = new File(path);
        System.out.print(p);
        if (!p.isDirectory()) p.mkdirs();
        if (!f.exists()) {
            try {
                f.createNewFile();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * �����ֵ
     * @param sec
     * @param key
     * @return
     */
    public String KeyValueRead(String sec,String key)
    {
        Wini ini = new Wini();
        try {
            ini.load(f);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return ini.get(sec,key);
    }

    /**
     * д���ֵ
     * @param sec
     * @param key
     * @param i
     */
    private void KeyValueWrite(String sec, String key, int i) {
		// TODO Auto-generated method stub
    	Object[] value = new Object[0];
    	value[0] = Integer.valueOf(i);
		KeyValueWrite(sec, key, value);
	}

    /**
     * д���ֵ
     * @param sec
     * @param key
     * @param value
     */
    public void KeyValueWrite(String sec,String key,Object value)
    {
        try {
            Wini ini = new Wini(f);
            ini.put(sec,key,value);
            ini.store();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
