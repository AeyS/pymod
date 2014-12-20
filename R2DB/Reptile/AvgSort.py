#coding:utf-8
'''
Created on 2014年7月15日

@author: TOM
'''

def generate(ls):
    n = 0
    plus = {}
    for i in ls:
        plus[n] = i
    return plus

class Average_sorting(object):
    """docstring for Average_sorting"""
    def __init__(self, widenum, textdir):
        super(Average_sorting, self).__init__()
        self.widenum = int(widenum)
        self.textdir = textdir
        # Meet the requirements of the combined group
        self.success_list = []
        self.b_split = []
        # 标题长度值数组;[function_name : max_min_mark]
        self.max_min = []
        self.max_c_v = 0

    def max_min_mark(self):
        '''每次重排前清空数组'''
        self.max_min = []
        for i in self.b_split:
            self.max_min.append(len(i))

    def del_list_value(self, list1, list2, n):
        '''删除队列内已使用的值'''
        del list1[n]
        del list2[n]
        # 重排数据
        self.max_min_mark()

    def sortcolumn(self):
        '''列数计算'''
        import text
        textlines = open(self.textdir, 'r').readlines()
        textlines = text.del_BL(textlines)
        from random import sample
        textlines = sample(textlines,len(textlines))
        line = ''
        too_long = 0
        for i in xrange(0, len(textlines)):
            too_long = 0
            lines = line
            line = '%s%s' % (line,textlines[i].replace('\n', ' '))
            print len(line)
            if len(line)>54:
                # print '>60 %s' % line.decode('gb2312').encode('utf-8')
                self.success_list.append(lines+'\n')
                # 直接清空
                line = textlines[i].replace('\n', ' ')
                # 给出超长信号
                too_long = 1
            # 最大限制widenum个一组
            if len(line.strip(" ").split(" "))%self.widenum == 0 and too_long == 0:
                # print 'zeng %s' % line.decode('gb2312').encode('utf-8')
                self.success_list.append(line+'\n')
                # 直接清空
                line = ''
        self.success_list.append(line+'\n')
        return self.success_list

    def merger_group(self):
        '''字数计算：初始化队列'''
        import text
        textlines = open(self.textdir, 'r').readlines()
        textlines = text.del_BL(textlines)
        # textlines = text.judge_key(textlines)
        for i in xrange(0, len(textlines)):
            self.b_split.append(textlines[i].replace('\n', ''))
        from random import sample
        self.b_split = sample(self.b_split,len(self.b_split))

    def ispush(self, lines):
        '''当不满足宽度的时候，追加标题，指导最接近宽度值为止'''
        result = lines
        while len(lines) <= self.widenum:
            if len(self.max_min) < 1:
                break
            else:
                print '每一行的宽度数值: %s' % self.max_min
                try:
                    print '追加：%s' % lines.decode('gb2312').encode('utf-8')
                except:
                    print "转码错误"
                # 先用最大值试试看
                max_seat = self.max_min.index(max(self.max_min))
                max_title = self.b_split[max_seat]
                # 不行再用最小值进行组合
                min_seat = self.max_min.index(min(self.max_min))
                min_title = self.b_split[min_seat]
                # 另外申请一个空间来存储未超过指定宽度的标题，一期lines超过可以恢复
                result = lines
                lines = '%s %s' % (lines, max_title)
                if len(lines) > self.widenum:
                    # 如果用最大值来组合，超出指定宽度的话，则使用最小值来进行组合
                    lines = '%s %s' % (result, min_title)
                    if len(lines) <= self.widenum:
                        # 如果组合不超过指定宽度，则将进行组合的最小标题从列表删除
                        self.del_list_value(self.max_min, self.b_split, min_seat)
                    else:
                        # 如果用最小的进行，依然不行，则直接返回结果
                        break
                elif len(lines) <= self.widenum:
                    # 如果组合不超过指定宽度，则将进行组合的最大标题从列表删除
                    self.del_list_value(self.max_min, self.b_split, max_seat)
        print '追加结束'
        return result

    def best_value(self):
        self.merger_group()
        self.max_min_mark()
        if len(self.max_min) != 0:
            while len(self.max_min) > 1:
                print '每一行的宽度数值: %s' % self.max_min
                max_seat = self.max_min.index(max(self.max_min))
                max_title = self.b_split[max_seat]
                # 预删除，防止最大最小为同一值
                self.del_list_value(self.max_min, self.b_split, max_seat)
                min_seat = self.max_min.index(min(self.max_min))
                min_title = self.b_split[min_seat]
                print '列表最大值座位:  %s 最小值座位:  %s' % (max_seat, min_seat)
                if len(max_title)+len(min_title) > self.widenum:
                    # 成立单条
                    lines = max_title
                    print "最大标题单独立一条 警告！需要手动处理"
                else:
                    # 成立双条，删除最大最小数据位置
                    lines = '%s %s' % (max_title, min_title)
                    print '成立双条'
                    min_seat = self.max_min.index(min(self.max_min))
                    self.del_list_value(self.max_min, self.b_split, min_seat)
                    lines = self.ispush(lines)
                if len(lines) <= self.widenum:
                    self.success_list.append(lines+'\n')
                else:
                    print "超出--------"

            print max_title.decode('gb2312').encode('utf-8')
            if len(self.b_split) > 0:
                '''当合并到最后，只剩下一个值时，也添加进去'''
                print '最后剩余列表项：%s' % self.b_split
                self.success_list.append(self.b_split[0])
        return self.success_list
# ==========================================
# 以下为第四代算法,有大漏洞,不可用

    def maxc_title(self):
        # 获取最次值
        # self.max_c_v为每次与self.widenum的间隔数
        # plus 为获取值的字典
        # 每次叠加都需要重新生成一次字典
        from run_count import sort
        plus = generate(self.max_min)
        s = sort(self.widenum, plus)
        if self.max_c_v == 0:
            self.max_c_v = s.max()[1]
            print "获取最大值:%s" % self.max_c_v
        id, self.max_c_v = s.max_c(self.max_c_v)
        print id
        return self.b_split[id], id

    def max_end(self, lines):
        # 获取叠加
        result = lines
        title, id = self.maxc_title()
        lines = '%s %s' % (lines, title)
        if len(lines) <= self.widenum:
            self.del_list_value(self.b_split, self.max_min, id)
            return self.max_end(lines)
        return result

    def beat(self):
        print '每一行的宽度数值: %s' % self.max_min
        lines, id = self.maxc_title()
        self.del_list_value(self.b_split, self.max_min, id)
        if len(lines) >= self.widenum:
            return lines
        return self.max_end(lines)

    def succ(self):
        self.merger_group()
        self.max_min_mark()
        if len(self.max_min) != 0:
            while len(self.max_min) > 1:
                self.max_c_v = 0
                lines = self.beat()
                self.success_list.append(lines+'\n')

            if len(self.b_split) > 0:
                '''当合并到最后，只剩下一个值时，也添加进去'''
                print self.b_split
                self.success_list.append(self.b_split[0])
        return self.success_list
# ==========================================


def sort_test(width):
    '''重排序测试
    width = 字符数'''
    import os
    os.system('notepad d:/name.txt')
    import text
    content = text.fread('d:/name.txt', rt='realines')
    content = text.lsord(content)
    text.fwrite('d:/name.txt', content)
    avg = Average_sorting(width, 'd:/name.txt')
    sucls = avg.best_value()
    text.fwrite('d:/name.txt', sucls)
    os.system('notepad d:/name.txt')
    return len(sucls)


def sort_column(nums,path):
    '''列数排序'''
    import os
    os.system('notepad %s' % path)
    import text
    content = text.fread('%s' % path, rt='realines')
    content = [i.lower() for i in content] # lower everyline into text.lsord()
    content = text.lsord(content)
    text.fwrite('%s' % path, content)
    avg = Average_sorting(nums, '%s' % path)
    sucls = avg.sortcolumn()
    text.fwrite('%s' % path, sucls)
    os.system('notepad %s' % path)
    print '------%d' % len(sucls)
    

if __name__ == '__main__':
    # from run_count import sort
    # s = sort(60, {1: 14, 2: 27, 3: 30, 4: 12, 5: 36, 6: 7, 7: 6, 8: 1, 9: 21, 10: 3, 11: 14, 12: 27, 13: 21})
    # max_v = s.max()[1]
    # print s.max_c(max_v)
    sort_column(3,('D:/临时/ali/name.txt').decode('utf-8').encode('gb2312'))
