package org.aeys.keyword.nearSort;

import java.util.ArrayList;
import java.util.List;

/**
 * ����һ�������������������������, ��������Json
 * @note ��ס������Աֻ����set��get��ͷ���Һ������ӵĵ�һ����ĸ�����д
 * @author Aeys
 * 2014/11/14
 */
public class Entry{
    private long id;         // ����id
    private String entry;    // ����
    private List entryArr = new ArrayList(); // �ִ��б�

    public void setId(long id){
        this.id=id;
    }

    public long getId() {
        return id;
    }

    public void setEntry(String entry){
        this.entry=entry;
    }

    public String getEntry(){
        return entry;
    }

    public void setEntryArr(List entryArr){
        this.entryArr=entryArr;
    }

    public List getEntryArr(){
        return entryArr;
    }
}