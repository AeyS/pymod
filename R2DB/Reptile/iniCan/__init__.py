# coding: utf-8
'''
Created on 2014年11月29日

@author: Aeys
'''

from bases import meIni


class canIni(meIni):
    def __init__(self, path):
        meIni.__init__(self, path)
        self.load()

    def setvalue(self, section, option, value):
        self.sets(section, option, value)

    def getvalue(self, section, option):
        return self.gets(section, option)

    def close(self):
        self.save()


def ajjlini(path, method):
    '''负责通过ini配置文件与按键精灵进行交互通信
        写入 pyini(path,'section-<key-<value')
        读取 pyini(path,'section-<key')
    '''
    result = ''
    melib = method.split('->')
    print len(melib)
    if len(melib) == 3:
        ini = canIni(path)
        ini.setvalue(melib[0], melib[1], melib[2])
    elif len(melib) == 2:
        ini = canIni(path)
        result = ini.getvalue(melib[0], melib[1])
    else:
        print "输入错误"
    ini.close()
    return result


if "__main__" == __name__:
    path = "C:/runfuc.ini"
    ajjlini(path, "runfunc->result->123")
