# coding:utf-8
'''
Created on 2014年9月17日

@author: Aeys
'''

class csvCan(object):
    def __init__(self, path):
        super(csvCan,self).__init__()
        self.path = path
        
    def csvdict(self):
        import csv
        csvObj = csv.DictReader(open(self.path,'rb'))
        for i in csvObj:
            print i

    def csvls(self):
        import csv
        csvObj = csv.reader(open(self.path,'rb'))
        for i in range(3,len(csvObj)):
            print i
        
if __name__ == '__main__':
    csv = csvCan('D:/\xcc\xd4\xb1\xa6\xc8\xce\xce\xf1/0909/\xb7\xd2\xb7\xbc2014\xc7\xef\xbc\xbe\xb8\xc4\xb0\xe6.csv')
    csv.csvls()