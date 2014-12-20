#coding:utf-8

class sort(object):
    def __init__(self, wdnum, dicts):
        super(sort, self).__init__()
        self.wdnum = wdnum
        self.dict = dicts

    def run_num(self, max_c=0, method='max'):
        '''求数组最值
                    他们每一个数都有一个唯一的id，以此去获取他们
        max_c = 差值
                    返回
            n = 最大值/最小值/差值
            loc = 数组座位id'''
        # 最值座位
        loc = n = 0
        if method == 'max-' or method == 'min':
            # 最大次值，先得到最大值,再将最大值赋值给n
            n = max_v = self.max()[1]
        if method == 'min-':
            # 最小次值，先得到最小值,再求宽度数-最小值的结果赋值给n，因为最小次值得差肯定比这个小
            min_v = self.min()[1]
            n = self.wdnum - min_v
        for id, v in self.dict.items():
            if method == 'max-':
                # 用求得的最大值，去减数组里的每个数，直到获取两者差最小的最大次值
                if max_v - v < n:
                    loc = id
                    if max_v - v < max_c+1:
                        # 如果最大值减当前值的差小于max_c等于是最大值-最大值，因取的是最次值，故舍去 < max_c+1的差值
                        break
                    n = max_v - v
            if method == 'min-':
                # 用求得的最小值，去减数组里的每个数，直到获取两者差最小的最小次值
                res = abs(min_v - v)
                print v, res, max_c+1, n
                if res < n:
                    if res < max_c+1:
                        # 如果最小值减当前值的差小于max_c等于是最小值-最小值，因取的是最次值，故舍去 < max_c+1的差值
                        print res, max_c
                        break
                    n = res
                    loc = id
            elif method == 'max':
                # 求最大值
                if v > n:
                    n = v
                    loc = id
            elif method == 'min':
                # 求最小值
                if v < n:
                    n = v
                    loc = id
        print '位置：%d' % loc, '差值：%s' % n
        return loc, n

    def max(self, max_c=0):
        '''最大值
                    返回
            n = 最大值
            loc = 数组座位id'''
        return self.run_num(max_c, method='max')

    def min(self, max_c=0):
        '''最小值
                    返回
            n = 最小值
            loc = 数组座位id'''
        return self.run_num(max_c, method='min')

    def max_c(self, max_v):
        '''最大次值
                    返回
            n = 差值
            loc = 数组座位id'''
        # 最大次值，先得到最大值,再将最大值赋值给n
        max_now = 0
        for id, v in self.dict.items():
            # 最大值减去当前值，直到获取两者差最小的最大次值
            if max_now < v < max_v:
                max_id = id
                max_v = v
        print max_id, max_v
        return max_id, max_v
        # return self.run_num(max_now, method='max-')

    def min_c(self, max_c=0):
        '''最大次值
                    返回
            n = 差值
            loc = 数组座位id'''
        return self.run_num(max_c, method='min-')