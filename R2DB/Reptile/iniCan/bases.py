# coding: utf-8
'''
Created on 2014年11月29日

@author: Aeys
'''

from ConfigParser import ConfigParser


class meIni(ConfigParser):
    def __init__(self, path):
        ConfigParser.__init__(self)
        self.path = path

    def load(self):
        return self.read(self.path)

    def save(self):
        return self.write(open(self.path, 'w'))

    def gets(self, section, option):
        try:
            return self.get(section, option)
        except Exception, e:
            raise IOError("请检查文件内是否有此键值，如果有请先调用reads后再使用gets\n%s" % e)

    def sets(self, section, option, value):
        if self.has_section(section) is False:
            self.add_section(section)
        return self.set(section, option, value)

    def delete_option(self, section, option):
        return self.remove_option(section, option)

    def delete_section(self, section):
        return self.remove_section(section)

    def exist_option(self, section, option):
        return self.has_option(section, option)

    def exist_section(self, section):
        return self.has_section(section)


if __name__ == "__main__":
    path = "C:/runfuc.ini"
    ini = meIni(path)
    # 在内存操作
    ini.sets("oomm", "func", "getAds")
    ini.sets("nojet", "hello", "123")
    ini.sets("runfunc", "func", "getAds")
    ini.load()
    print ini.gets("runfunc", "func")
    ini.delete_section("oomm")
    ini.delete_option("nojet", "hello")
    # 保存到硬盘
    ini.save()
