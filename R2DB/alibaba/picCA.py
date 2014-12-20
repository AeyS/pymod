#coding:utf-8
'''
Created on 2014年11月20日

@author: Aeys
'''

def getpic(dbpath, path):
    '''bs4获取图片地址，文件名'''
    from Reptile import text
    from Reptile import html
    from taobao import picCA
    import os
    os.system('notepad %s' % path)
    basemsg_ls = html.get_attr(text.fread(path), 'dt.clr')
    for basemsg in basemsg_ls:
        basemsg = basemsg.prettify()
        src = text.regex(basemsg,r'value="(http://.*?)"','s')
        name = text.regex(basemsg,r'title="(.[^-]*?)">','s')
        print src.group(1),name.group(1)
        picCA.updatesrc2db(dbpath, src.group(1), name.group(1))
