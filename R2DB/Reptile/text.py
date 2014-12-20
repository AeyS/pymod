# coding:utf-8
'''
Created on 2014年7月15日

@author: TOM
'''
import os

def prls(ls):
    '''将多层列表内容全部打印出来
        ls = 列表'''
    for i in ls:
        if type(i) == type([]):
            prls(ls)
        else:
            print i


def lsord(ls):
    '''删除列表重复，保留唯一值
        ls = 列表'''
    for i in ls:
        while ls.count(i) > 1:
            ls.remove(i)
    return ls


def pathsplit(path):
    '''分割文件路径
        path = 文件路径'''
    d, f = os.path.split(path)
    return {'dir': d, 'file': f, 'name': ".".join(f.split('.')[0:-1]), \
            'format': f.split('.')[-1]}

import cPickle


class Inis(object):
    '''将动态数据保存到配置文件'''
    def __init__(self, inipath):
        super(Inis, self).__init__()
        self.inipath = inipath

    def write(self, obj):
        '''写入文件
            obj = 数据对象'''
        f = open(self.inipath, 'w')
        cPickle.dump(obj, f)
        f.close()

    def load(self):
        '''载入文件数据'''
        f = open(self.inipath, 'r')
        obj = cPickle.load(f)
        f.close()
        return obj


def isfile(path):
    '''判断路径是否文件
        path = 文件路径'''
    return os.path.isfile(path)


def findx(word, text, n, ls=[]):
    '''寻找单词在文本中出现的所有位置
        word = 单词
        text = 文本
        n = 文本开始查找位置
        ls = 保存单词出现的所有位置'''
    n = text.find(word, n, len(text))
    if n > -1:
        ls.append(n)
        print n
        findx(n + 1, text)
    return ls


def stdo(string, filepath, m='w'):
    '''打开文件，写入数据
        string = 数据
        filepath = 文件路径
        m = 写入方法(a+,w)'''
    import sys
    with open(filepath, m) as hdle:
        temp = sys.stdout
        sys.stdout = hdle
        print string
        sys.stdout = temp


def Transcoding(data):
    '''自检测文本编码并转码数据为UNICODE
        data = 文本数据'''
    import chardet
    try:
        enc = chardet.detect(data)['encoding']
        return data.decode(enc, 'ignore')  # Ignore the angle char
    except Exception, e:
        print e
        return data


def regex(string, reg, m='f', re_str='', G=False):
    '''正则函数
        string = 文本
        reg = 正则表达式
        m = 正则方法
        re_str = 替换成字符
        G = 以下任何表达

    re.I == IGNORECASE  使匹配对大小写不敏感；字符类和字符串匹配字母时忽略大小写。\
            举个例子，[A-Z]也可以匹配小写字母，Spam 可以匹配 "Spam", "spam", 或 "spAM"。\
            这个小写字母并不考虑当前位置。
    re.S == DOTALL     使 "." 特殊字符完全匹配任何字符，包括换行；没有这个标志， "." 匹配除了换行外的任何字符。
    re.L == LOCALE     影响 "w, "W, "b, 和 "B，这取决于当前的本地化设置。locales 是 C 语言库中的一项功能，\
            是用来为需要考虑不同语言的编程提供帮助的。举个例子，如果你正在处理法文文本，你想用 "w+ 来匹配文字，\
            但 "w 只匹配字符类 [A-Za-z]；它并不能匹配 "é" 或 "?"。如果你的系统配置适当且本地化设置为法语，\
            那么内部的 C 函数将告诉程序 "é" 也应该被认为是一个字母。当在编译正则表达式时使用 LOCALE 标志会得到用 \
            这些 C 函数来处理 "w 後的编译对象；这会更慢，但也会象你希望的那样可以用 "w+ 来匹配法文文本。
    re.M == MULTILINE   (此时 ^ 和 $ 不会被解释; 它们将在 4.1 节被介绍.) 使用 "^" 只匹配字符串的开始，\
            而 $ 则只匹配字符串的结尾和直接在换行前（如果有的话）的字符串结尾。当本标志指定後，"^" 匹配字符串的开始和字符串中每行的开始。\
            同样的， $ 元字符匹配字符串结尾和字符串中每行的结尾（直接在每个换行之前）。
    re.X == VERBOSE    该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。当该标志被指定时，在 RE 字符串中的空白符被 \
            忽略，除非该空白符在字符类中或在反斜杠之後；这可以让你更清晰地组织和缩进 RE。它也可以允许你将注释写入 RE，\
            这些注释会被引擎忽略；注释用 "#"号 来标识，不过该符号不能在字符串或反斜杠之後。
    '''
    import re
    if G:
        if G == 're.S':
            #对大小写不敏感
            r = re.compile(reg, re.S)
        if G == 're.I':
            #忽略换行符
            r = re.compile(reg, re.I)
    else:
        r = re.compile(reg)
    try:
        if m == 's':
            return r.search(string)
        elif m == 'm':
            return r.match(string)
        elif m == 'f':
            return r.findall(string)
        elif m == 'r':
            return r.sub(re_str, string)
    except Exception, e:
        print e
        return 0


def pathls(dirname, m=0, key='.txt'):
    """获取该路径下所有文件列表
        dirname = 路径
        m = 返回绝对路径 1是 0否
        key = 指定返回文件的格式类型"""
    if dirname[-1] != '/':
        dirname = dirname + '/'
    if m:
        filels = [dirname + i for i in os.listdir(dirname)]
    else:
        filels = os.listdir(dirname)
    if key != '':
        return [i for i in filels if key in i]
    return filels


def copyfile(oldpath, newpath):
    '''拷贝文件
        oldpath = 旧文件
        newpath = 新文件'''
    import shutil
    return shutil.copyfile(oldpath, newpath)


def fread(path, m='r', u=False, rt='read'):
    """读取文件
        fread(path,m='r')
        m = 读取方法
            fread(path,{'loc':n,'sec':m}
            ｛loc = 开始读取文本位置，sec = 读取文本段落长度｝
        u = 为是否转换为unicode
        rt = 返回结果（str=字符串，ls为列表）
    """
    # path = Transcoding(path)
    if type(m) == type({}):
        f = open(path, 'r')
        f.seek(m['loc'])
        res = f.read(m['sec'])
    else:
        f = open(path, m)
        if rt == 'read':
            res = f.read()
        elif rt == 'realines':
            res = f.readlines()
        else:
            raise '请指定返回值！'
    f.close()
    if u:
        return Transcoding(res)
    return res


def fwrite(path, cont, m='w', u=False):
    '''写入文件
        path = 路径
        cont = 文本
        m = 方法'''
    string = ''
    f = open(path, m)
    if type(cont) == type([]):
        string = ''.join(cont)
    else:
        string = cont
    if u is True:
        string = string.encode('gb2312')
    f.write(string)
    f.close()


def random(n, x):
    '''随机数
        n = 最小范围
        x = 最大范围'''
    import random
    return random.randint(n, x)


#---->            old code        <----#

def filepath(fp, mothod=False):
    u'#\u5c06\u6587\u4ef6\u4fdd\u5b58\u7684\u8def\u5f84\u505a\u4e00\u4e2a\u9884\u5904\u7406\uff0c\u5df2\u7ed9\u51fa\u8def\u5f84\u8c03\u7528\u65f6\u53ea\u9700\u586b\u5199\u6587\u4ef6\u540d\u5373\u53ef\uff01'
    if fp == 'xh':
        path = u'D:/\u4e34\u65f6/ali/' + fp + '.txt'
    elif fp == 'jg':
        path = u'D:/\u4e34\u65f6/ali/' + fp + '.txt'
    elif ':' or '\\' or '/' in fp:
        path = fp
    else:
        path = u'D:/\u4e34\u65f6/ali/pump/' + fp + '.txt'
    uipath = unicode(path)
    f2 = judge_file(uipath, mothod)
    return f2, uipath

def Copywt():
    '''Copy text written to file.'''
    u'#\u5173\u952e\u8bcd\u91cd\u590d\u5199\u5165n\u904d\u5230\u6587\u4ef6\u91cc'
    path = raw_input('filepath:')
    result = []
    while True:
        con = raw_input('please:')
        if con == '': break
        nx = raw_input('sum:')
        x = 0
        while x < nx:
            result.append('%s\n' % con)
            x += 1
    wlist(result, path, True)

def judge_file(path, mothod):
    '''If have old file,del old file,creatr new file.

        mothod = a+,w [and so on...]
        return file handle'''
    if mothod == False: mothod = 'a+'
    elif mothod == True: raise IOError('Must is a+,w [and so on...]')
    u'#\u83b7\u53d6\u6587\u4ef6\u8def\u5f84\uff0c\u53ca\u6587\u4ef6\u540d\u3002'
    dirname, filename = os.path.split(path)
    if os.path.isdir(dirname) == False: os.makedirs(dirname)
    if os.path.isfile(path): os.remove(path)
    else: print 'This is new file!  >>" %s "' % path
    return open(path, mothod)

def getlines(files, start, end=False):
    '''Gets the specified row.

        files = a list
        start = start rows
        end = end rows'''
    getline = []
    if type(files) != list: raise TypeError('Parameter 1 not a list')
    if end is False: end = start + 1
    for line in files[start:end]:
        getline.append(line)
    return getline

def wlist(list_a, ad, overflow=False, mothod=False):
    u'#\u5c06\u5217\u8868\u5199\u5165\u6587\u6863'
    def wt(list, f):
        for x in xrange(0, len(list)):
            f.writelines(list[x])
        return x
    f2, path = filepath(ad, mothod)
    overflows = ''
    n = wt(list_a, f2)
    if overflow:
        overflows = '\xd2\xe7\xb3\xf6'
        f2.write(overflows)
        overflows = '\n>>Add endlines\t%s' % unicode(overflows , "gbk")
        n += 1
    f2.close()
    print 'Generate %s line: %d %s' % (path, n, overflows)


def del_BL(list):
    u'\u5220\u9664\u7a7a\u767d\u884c'
    list_a = []
    for i in [line for line in list if len(line) > 2]:
        if len(i.replace('"', '')) > 2: list_a.append(i)
    return list_a

def judge_key(list, w=0):
    u'''\u5904\u7406\u5217\u8868\u91cc\u7684\u5e26\u6570\u5b57\u5173\u952e\u8bcd,judge
 pump have sum,if have jump out\n\t0 flist\u662f\u8fd4\u56de\u4e00\u4e2a\u5173\u952e\u8bcd\u91cc\u542b\u6570\u5b57\u9664\u5916\u7684\u5217\u8868\n\t2 flist_list
\u662f\u8fd4\u56de\u4e00\u4e2a\u629b\u5f03\u6240\u6709\u5305\u542b\u5173\u952e\u8bcd\u7684\u5217\u8868\n\t1 flist_t\u662f\u5c06\u88ab\u5254\u9664\u7684\u5185\u5bb9\u5199\u5165\u4ee5\u7528\u6765\u5224\u65ad\u7684\u5173\u952e\u8bcd\u547d\u540d\u7684\u6587\u6863'''
    judge_key = raw_input('judge_key:')
    flist = []
    flist_t = []
    flist_list = []
    w = int(w)
    key = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    for line in [line for line in list if len(line) > 3]:
        if judge_key in line:
            if [k for k in key if k in line]:
                print "%s Have Sum" % judge_key
                flist_t.append(line)
                break
            print "%s Not Sum" % judge_key
            flist.append(line)
            flist_t.append(line)
        else:
            flist.append(line)
            flist_list.append(line)

    if w is 1:
        print 'w=%s Get Single Keyword Mode' % w
        wlist(flist_t, 'd:/name_%s.txt' % judge_key)
    elif w is 2:
        print 'w=%s Discard single keyword mode' % w
        return flist_list
    else:
        print 'w=%s In addition to figures contain keywords' % w
        return flist
    
'''************************************'''

def list_del_list(list_a, list_b):
    u'''\u63d0\u4f9b\u4ef7\u683c\u5217\u8868\uff0c\u5750\u53c2\u8003\u5220\u9664\u578b
\u53f7\u5217\u8868\u5185\u5bb9\u53ca\u51e0\u4e2a\u5217\u8868\u81ea\u8eab\u7684\u5185\u5bb9\n\tlist_b\u9700\u8981\u5904\u7406\u7684\u6587\u4ef6\uff0clist_a\u7528
\u6765\u5bf9\u6bd4\u7684\u6587\u4ef6'''
    path_xh = 'D:/file_contrast.txt'
    path_jg = 'D:/file_handle.txt'
    sum_list = []
    jg_list = []
    n_jg = 0
    for x in list_a:
        if len(x) < 3:
            u'''\u4ee5\u957f\u5ea6\u5c0f\u4e8e3\u6765\u5224\u65ad\u2018/\u2019\u7a7a\u767d\u9879\u7684\u4f4d\u7f6e\uff0c\u5e76\u6536\u96c6\u5728sum_list\u91cc'''
            sum_list.append(n_jg)
            print n_jg, x,
        else:
            u'\u8fd9\u4efd\u4ef7\u683c\u5217\u8868\u5c31\u5254\u9664\u4e86\u2018/\u2019\u7a7a\u767d\u9879'
            jg_list.append(x)
        n_jg += 1
    n = 0
    for k in sum_list:
        u'''\u8fd9\u4efd\u578b\u53f7\u5217\u8868\u5c31\u5254\u9664\u4e86\u2018/\u2019\u7a7a\u767d\u9879\uff0c\u56e0\u4e3a\u6bcf\u5220\u9664\u4e00\u9879\uff0c\u5217\u8868\u603b\u6570\u5c31\u51cf\u5c111\uff0c\u6240\u4ee5\u5220\u9664\u4e00\u9879\u7684\u4f4d\u7f6e\u5c31\u5f97\u901a\u8fc7-n\u6b21\u6765\u83b7\u53d6\u3002'''
        k = k - n
        del list_b[k]
        print 'del%s' % k
        n += 1
    wlist(jg_list, path_jg)
    wlist(list_b, path_xh)

def split_h(f):
    path = raw_input('path:')
    var = raw_input('split(...):')
    location_sum = raw_input('location_sum:')
    result = []
    for i in f:
        content = i.split(var)[int(location_sum)]
        result.append('%s\n' % content.replace('\n', ''))
    wlist(result, path)
