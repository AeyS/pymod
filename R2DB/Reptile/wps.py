#coding:utf-8
'''
Created on 2014年7月15日

@author: TOM
'''
import win32com.client

class Word:
    def __init__(self, filename=None):
        '''操作wps的组件'''
        self.docApp = win32com.client.Dispatch('wps.Application')
        if filename:
            self.filename = filename
            self.Documents = self.docApp.Documents.Open(filename)
        else:
            self.Documents = self.docApp.Documents.Add()
            self.filename = ''
            self.Tables = ''
            
            
    def save(self, newfilename):
        if newfilename:
            if '.pdf' in newfilename:
                self.filename = newfilename
                self.Documents.ExportPdf(newfilename)
            else:
                self.filename = newfilename
                self.Documents.SaveAs(newfilename)
        else:
            self.Documents.Save()
            
    
    def close(self):
        self.Documents.Close(SaveChanges=0)
        del self.docApp

    def write(self,content,s=0,e=0):
        self.myRange = self.Documents.Range(s,e)
        self.myRange.InsertBefore(content)
    
    def style(self):
        self.myRange
    
    def table(self):
        self.myRange = self.Documents.Range(0, 0)
        self.Tables = self.docApp.Tables.Add(self.myRange, 5)
        self.Tables(1).Rows(1).HeadingFormat = True
    
    def getRange(self, row1, col1, row2, col2):
        "return a 2d array (i.e. tuple of tuples)"
        sht = self.Documents
        return sht.Range(sht.Cells(row1, col1), sht.Cells(row2, col2)).Value
    
    
    
class Excel:
    """A utility to make it easier to get at Excel.    Remembering
    to save the data is your problem, as is    error handling.
    Operates on one workbook at a time."""
    
    def __init__(self, filename=None):
        self.xlApp = win32com.client.Dispatch('et.Application')
        if filename:
            self.filename = filename
            self.xlBook = self.xlApp.Workbooks.Open(filename)
        else:
            self.xlBook = self.xlApp.Workbooks.Add()
            self.filename = ''  
    
    def save(self, newfilename=None):
        if newfilename:
            if '.pdf' in newfilename:
                self.filename = newfilename
                self.xlBook.ExportPdf(newfilename)
            else:
                self.filename = newfilename
                self.xlBook.SaveAs(newfilename)
        else:
            self.xlBook.Save()    
    
    def close(self):
        self.xlBook.Close(SaveChanges=0)
        del self.xlApp
    
    def getCell(self, sheet, row, col):
        "Get value of one cell"
        sht = self.xlBook.Worksheets(sheet)
        return sht.Cells(row, col).Value
    
    def setCell(self, sheet, row, col, value):
        "set value of one cell"
        sht = self.xlBook.Worksheets(sheet)
        sht.Cells(row, col).Value = value
    
    def getRange(self, sheet, row1, col1, row2, col2):
        "return a 2d array (i.e. tuple of tuples)"
        sht = self.xlBook.Worksheets(sheet)
        return sht.Range(sht.Cells(row1, col1), sht.Cells(row2, col2)).Value
    
    def addPicture(self, sheet, pictureName, Left, Top, Width, Height):
        "Insert a picture in sheet"
        sht = self.xlBook.Worksheets(sheet)
        sht.Shapes.AddPicture(pictureName, 1, 1, Left, Top, Width, Height)
    
    def cpSheet(self, before):
        "copy sheet"
        shts = self.xlBook.Worksheets
        shts(1).Copy(None,shts(1))