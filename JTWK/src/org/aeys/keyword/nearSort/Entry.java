package org.aeys.keyword.nearSort;

import java.util.ArrayList;
import java.util.List;

/**
 * 这是一个词条容器，存放索引及内容, 用于制作Json
 * @note 记住方法成员只能以set或get开头并且后面连接的第一个字母必须大写
 * @author Aeys
 * 2014/11/14
 */
public class Entry{
    private long id;         // 索引id
    private String entry;    // 词条
    private List entryArr = new ArrayList(); // 分词列表

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